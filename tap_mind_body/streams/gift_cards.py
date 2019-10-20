from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class GiftCardsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'gift_cards'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'GiftCards'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/giftcards'
