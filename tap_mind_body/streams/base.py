import math
import pytz
import singer
import singer.utils
import singer.metrics
import singer.transform

from datetime import timedelta, datetime


from tap_framework.streams import BaseStream as base


LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ['id']
    FIELDS_TO_IGNORE = []  
            
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
            #development limit    
######REMOVE BEFORE MERGING
            if offset > 20:
                break     
            else:
                offset += limit
                if self.REQUIRES:
                    params = self.get_params(parent['Id'], offset, limit)
                else:
                    params = self.get_params(offset, limit)
                
                
    def sync_unpaginated(self, params, url):            
        table = self.TABLE 
        self.get_stream_data(url, params)
    
    def get_url(self):
        return 'https://api.mindbodyonline.com/public/v6{}'.format(self.path)
        
    def get_params(self, offset_value=0, limit_value=10):
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
                            
    def transform_stream_data(self, response):
        transformed = []
        for record in response[self.RESPONSE_KEY]:
            record = self.transform_record(record) 
            transformed.append(record)

        return transformed


    def read_pagination_response(self, response, key):
        if 'PaginationResponse' not in response:
            raise ValueError('Got invalid pagination response')
        if key not in response['PaginationResponse']:
            raise ValueError('Key {} not found in pagination response'.format(key))     
        value = response['PaginationResponse'][key]
        
        return value