from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class LocationsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'locations'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Locations'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/site/locations'
