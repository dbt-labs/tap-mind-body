from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClientIndexesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'client_indexes'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'ClientIndexes'
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/client/clientindexes'
