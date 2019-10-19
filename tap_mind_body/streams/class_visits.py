from tap_mind_body.streams.base import ChildStream
from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassVisitsStream(ChildStream):
    API_METHOD = 'GET'
    TABLE = 'class_visits'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['classes']

        
    @property
    def path(self):
        return '/class/classvisits'
      
    def sync_data(self, parent):
        LOGGER.info('this is the class_visits sync_data method')
        self.sync_data_unpaginated(parent)
        
    def get_params(self, class_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClassID': class_id
        }
        return params
        
                
    def get_stream_data(self, response):
        LOGGER.info('syncing info for {}'.format(self))
        transformed = []
        for record in response['Class']['Visits']:
            ## removes fields with missing/wrong data type
            #record = self.transform_record(record) 
            transformed.append(record)

        return transformed            