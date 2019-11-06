from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class SessionTypesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'session_types'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'SessionTypes'
    IS_PAGINATED = True

    @property
    def path(self):
        return '/site/sessiontypes'
        
    def get_params(self, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value
        }
        return params    