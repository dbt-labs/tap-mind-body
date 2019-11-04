from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class CrossReigonalClientAssociationsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'cross_reigional_client_associations'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['clients']
    RESPONSE_KEY = 'CrossRegionalClientAssociations'
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/client/crossregionalclientassociations'
        
    def get_params(self, client_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClientID': client_id
        }
        return params       