from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ActiveClientMembershipsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'active_client_memberships'
    KEY_PROPERTIES = ['Id']
    REQUIRES = ['clients']
    RESPONSE_KEY = 'ClientMemberships'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'RestrictedLocations'
    ]
        
    @property
    def path(self):
        return '/client/activeclientmemberships'
        
    def get_params(self, client_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClientID': client_id
        }
        return params        