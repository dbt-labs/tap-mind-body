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
    
    def sync_data(self):
        table = self.TABLE

        LOGGER.info('Syncing data for {}'.format(table))
        url = self.get_url()

        while True:
            response = self.client.make_request(url, self.API_METHOD)
            transformed = self.get_stream_data(response)

            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))
            
            #temporary fix to end loop
            if len(transformed) < 100:            
                return 
        
                            

    def get_stream_data(self, response):
        #LOGGER.info('the response is {} of type {}'.format(response, type(response)))
        transformed = []
        for record in response['Classes']:
            #LOGGER.info('the record is {} of type {}'.format(record, type(record)))
            ## removes fields with missing/wrong data type
            #record = self.transform_record(record) 
            transformed.append(record)

        return transformed
