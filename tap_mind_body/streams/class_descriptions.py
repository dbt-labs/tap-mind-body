from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassDescriptionsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'class_descriptions'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'ClassDescriptions'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/class/classdescriptions'
