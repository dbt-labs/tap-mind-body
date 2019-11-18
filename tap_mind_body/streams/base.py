import math
import pytz
import singer
import singer.utils
import singer.metrics
import singer.transform

from datetime import timedelta, datetime
from tap_framework.streams import BaseStream as base
from tap_mind_body.state import incorporate, get_last_record_value_for_table


LOGGER = singer.get_logger()
        
class BaseStream(base):
    KEY_PROPERTIES = ['Id']
    FIELDS_TO_IGNORE = []  
    
    def sync(self):
        LOGGER.info('Syncing stream {} with {}'
                    .format(self.catalog.tap_stream_id,
                            self.__class__.__name__))
                            
        self.write_schema()
        
        for stream in self.substreams:
            singer.write_schema(
                stream.TABLE, 
                stream.catalog.schema.to_dict(), 
                stream.KEY_PROPERTIES
            )
        return self.sync_data()
                    
    # determines sync function based on expected response        
    def sync_data(self, parent=None):
        url = self.get_url()
        # if child object -> provides parent id in parameter
        if self.REQUIRES:
            params = self.get_params(parent['Id'])
        else:
            params = self.get_params()
                    
        if self.IS_PAGINATED:
            self.sync_paginated(params, url, parent)
        else:
            self.sync_unpaginated(params, url)
    
    
    def sync_paginated(self, params, url, parent=None):            
        table = self.TABLE
            
        while True:
            response, transformed = self.get_stream_data(url, params)

            # error handling for unexpected responses
            if response is None:
                break    
                
            # syncs all children given current parent id    
            for stream in self.substreams:
                for record in transformed:
                    stream.sync_data(record)
                    
            num_results = self.read_pagination_response(response, 'PageSize')
            offset = self.read_pagination_response(response, 'RequestedOffset')
            total_results = self.read_pagination_response(response, 'TotalResults')
            limit = params['limit']
            
            if num_results < limit:
                break
            else:
                offset += limit
                if self.REQUIRES:
                    params = self.get_params(parent['Id'], offset, limit)
                else:
                    params = self.get_params(offset, limit)
                    if transformed:
                        last_record = transformed[-1]
                        self.save_state(last_record)
                    else:
                        LOGGER.info('no record to save')
                
                
    def sync_unpaginated(self, params, url):            
        table = self.TABLE 
        self.get_stream_data(url, params)
    
    def get_url(self):
        return 'https://api.mindbodyonline.com/public/v6{}'.format(self.path)
        
    def get_params(self, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value
        }
        return params
        
    # makes request and returns transformed records    
    def get_stream_data(self, url, params):
        table = self.TABLE
        LOGGER.info('Syncing data for {}'.format(table))
        response = self.client.make_request(url, self.API_METHOD, params)
        transformed = self.transform_stream_data(response)
        
        with singer.metrics.record_counter(endpoint=table) as counter:
            singer.write_records(table, transformed)
            counter.increment(len(transformed))
        
        return response, transformed  
        
    # overwrites framework function to remove unwanted fields within the response
    def transform_record(self, record):
        with singer.Transformer() as tx:
            metadata = {}

            if self.catalog.metadata is not None:
                metadata = singer.metadata.to_map(self.catalog.metadata)
                
                for field in self.FIELDS_TO_IGNORE:
                    try:
                        del record[field]
                    except KeyError:
                        LOGGER.info('{} does not exist in current record'
                                    .format(field))
                            
            return tx.transform(
                record,
                self.catalog.schema.to_dict(),
                metadata)    
    
    # parses response and transforms using singer framework                        
    def transform_stream_data(self, response):
        transformed = []
        for record in response[self.RESPONSE_KEY]:
            record = self.transform_record(record) 
            transformed.append(record)

        return transformed

    # parses pagination response    
    def read_pagination_response(self, response, key):
        if 'PaginationResponse' not in response:
            raise ValueError('Got invalid pagination response')
        if key not in response['PaginationResponse']:
            raise ValueError('Key {} not found in pagination response'.format(key))     
        value = response['PaginationResponse'][key]
        
        return value
        
    def get_start_date(self):
        bookmark = get_last_record_value_for_table(self.state, self.TABLE)
        if bookmark:
            return bookmark
        else:
            return self.config['start_date']
                 
    def save_state(self, last_record):
        LOGGER.info('the last record is {}'.format(last_record))
        if 'LastModifiedDateTime' in last_record:
            LOGGER.info('starting to save')
            last_modified_date = last_record['LastModifiedDateTime']
            self.state = incorporate(self.state, self.TABLE, "LastModifiedDateTime", last_modified_date)
            LOGGER.info('Updating state. with {}'.format(self.state))
            singer.write_state(self.state)