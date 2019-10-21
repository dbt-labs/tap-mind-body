from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ServicesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'services'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'Services'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/services'
