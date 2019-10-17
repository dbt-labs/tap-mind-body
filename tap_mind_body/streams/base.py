import math
import pytz
import singer
import singer.utils
import singer.metrics

from datetime import timedelta, datetime


from tap_framework.streams import BaseStream as base


LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ['id']

    def get_url(self):
        return 'https://api.mindbodyonline.com/public/v6{}'.format(self.path)
        
    def get_params(self, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value
        }
        
        return params
    
    def sync_data(self):
        table = self.TABLE

        LOGGER.info('Syncing data for {}'.format(table))
        url = self.get_url()
        params = self.get_params()

        while True:
            ##LOGGER.info('making request with url {}, method {}, and parameter {}'.format(url, self.API_METHOD, params))
            response = self.client.make_request(url, self.API_METHOD, params)
            transformed = self.get_stream_data(response)
            num_results = self.read_pagination_response(response, 'PageSize')
            offset = self.read_pagination_response(response, 'RequestedOffset')
            limit = params['limit']
            
            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))

            for stream in self.substreams:
                for record in transformed:
                    stream.sync_data(record)
            
            #temporary fix to end loop
            if num_results < limit:            
                break 
            else:
                offset += limit
                params = self.get_params(offset, limit)
        
                            

    def get_stream_data(self, response):
        #LOGGER.info('the response is {} of type {}'.format(response, type(response)))
        transformed = []
        for record in response[self.RESPONSE_KEY]:
            #LOGGER.info('the record is {} of type {}'.format(record, type(record)))
            ## removes fields with missing/wrong data type
            #record = self.transform_record(record) 
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
    def get_parent_id(self, parent):
        raise NotImplementedError('get_parent_id is not implemented!')

    def sync_data(self, parent=None):
        raise NotImplementedError(
            'sync_data is not implemented!')
