from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class SalesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'sales'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'Sales'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/sales'
