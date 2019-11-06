from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ProgramsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'programs'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Programs'
    IS_PAGINATED = True

    @property
    def path(self):
        return '/site/programs'
