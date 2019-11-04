from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClientAccountBalancesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'client_account_balances'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['clients']
    RESPONSE_KEY = 'Clients'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/client/clientaccountbalances'
        
    def get_params(self, client_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClientIDs': client_id
        }
        return params       