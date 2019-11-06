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
