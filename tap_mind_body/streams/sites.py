from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class SitesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'sites'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Sites'
    IS_PAGINATED = True

    @property
    def path(self):
        return '/site/sites'
