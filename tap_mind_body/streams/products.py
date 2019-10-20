from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ProductsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'products'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'Products'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/products'
