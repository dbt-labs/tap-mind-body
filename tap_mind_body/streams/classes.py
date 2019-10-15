from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'classes'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'Classes'

        
    @property
    def path(self):
        return '/class/classes'
