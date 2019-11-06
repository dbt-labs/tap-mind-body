from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class CustomPaymentMethodsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'custom_payment_methods'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'PaymentMethods'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/sale/custompaymentmethods'
