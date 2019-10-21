from tap_mind_body.streams.base import ChildStream
from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ContractsStream(ChildStream):
    API_METHOD = 'GET'
    TABLE = 'contracts'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['locations']
    RESPONSE_KEY = 'Contracts'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/contracts'
        
    def get_params(self, location_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'LocationId': location_id
        }
        return params
  