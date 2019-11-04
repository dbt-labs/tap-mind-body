from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ResourcesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'resources'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'Resources'
    IS_PAGINATED = True

    @property
    def path(self):
        return '/site/resources'
