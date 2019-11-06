from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class CustomClientFieldsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'custom_client_fields'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'CustomClientFields'
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/client/customclientfields'
