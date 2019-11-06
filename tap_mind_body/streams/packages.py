from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class PackagesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'packages'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Packages'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/packages'
