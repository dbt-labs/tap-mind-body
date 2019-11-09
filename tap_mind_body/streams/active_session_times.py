from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ActiveSessionTimesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'active_session_times'
    KEY_PROPERTIES = ['Id']
    IS_PAGINATED = True

    @property
    def path(self):
        return '/appointment/activesessiontimes'
        
    def get_params(self, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'scheduletype': 'all'
        }
        return params    
        
    def transform_stream_data(self, response):
        transformed = []
        for record in response['ActiveSessionTimes']:
            record = self.transform_record({'active_session_times': record, 'Id':hash(record)}) 
            transformed.append(record)

        return transformed    