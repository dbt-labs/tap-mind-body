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

    def get_url(self):
        return 'https://api.mindbodyonline.com/public/v6{}'.format(self.path)
        
    def get_params(self, offset_value=0, limit_value=25):
        params = {
            'offset': offset_value,
            'limit': limit_value
        }
        
        return params
    
    def sync_data(self, parent=None):
        table = self.TABLE

        LOGGER.info('Syncing data for {}'.format(table))
        url = self.get_url()
        params = self.get_params()

        while True:
            response = self.client.make_request(url, self.API_METHOD, params, body=None)
            transformed = self.get_stream_data(response)
            
            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))
            
            for stream in self.substreams:
                for record in transformed:
                    stream.sync_data(record)    
                    
            if self.IS_PAGINATED:
                num_results = self.read_pagination_response(response, 'PageSize')
                offset = self.read_pagination_response(response, 'RequestedOffset')
                limit = params['limit']
                
                if num_results < limit:            
                    break 
                else:
                    offset += limit
                    params = self.get_params(offset, limit)  
            else:
                break          
    
    def transform_record(self, record):
        with singer.Transformer() as tx:
            metadata = {}

            if self.catalog.metadata is not None:
                metadata = singer.metadata.to_map(self.catalog.metadata)
                
                for field in self.FIELDS_TO_IGNORE:
                    try:
                        del record[field]
                    except KeyError:
                        LOGGER.info('{} does not exist in current record')
                            
            return tx.transform(
                record,
                self.catalog.schema.to_dict(),
                metadata)    
                            
    def get_stream_data(self, response):
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
        

class ChildStream(BaseStream):
    def sync_data(self, parent=None):
        table = self.TABLE
        
        if parent is None:
            raise RuntimeError("Parent is required in substream {}".format(table))

        LOGGER.info('Syncing data for {}'.format(table))
        url = self.get_url()
        params = self.get_params(parent['Id'])

        while True:
            response = self.client.make_request(url, self.API_METHOD, params, body=None)
            transformed = self.get_stream_data(response)
            
            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))
            
            if self.IS_PAGINATED:
                num_results = self.read_pagination_response(response, 'PageSize')
                offset = self.read_pagination_response(response, 'RequestedOffset')
                limit = params['limit']
                
                if num_results < limit:            
                    break 
                else:
                    offset += limit
                    params = self.get_params(parent['Id'], offset, limit)
            else:
                break        