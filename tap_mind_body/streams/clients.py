from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClientsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'clients'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Clients'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'CustomClientFields',
        'SalesReps'
    ]
        
    @property
    def path(self):
        return '/client/clients'
        
    def get_params(self, offset_value=0, limit_value=200):
        last_modified_date = self.get_start_date()
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'LastModifiedDate': last_modified_date
        }
        return params    