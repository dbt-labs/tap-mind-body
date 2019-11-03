from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassVisitsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'class_visits'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['classes']
    IS_PAGINATED = False
    PARENT_ID = 'ClassID'

        
    @property
    def path(self):
        return '/class/classvisits'
        
    def get_params(self, class_id, offset_value=0, limit_value=10):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClassID': class_id
        }
        return params
        
                
    def transform_stream_data(self, response):
        transformed = []
        for record in response['Class']['Visits']:
            record = self.transform_record(record) 
            transformed.append(record)

        return transformed            