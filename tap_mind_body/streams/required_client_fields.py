from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class RequiredClientFieldsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'required_client_fields'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'RequiredClientFields'
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/client/requiredclientfields'

    def transform_stream_data(self, response):
        transformed = []
        for record in response['RequiredClientFields']:
            record = self.transform_record({'required_fields': record}) 
            transformed.append(record)

        return transformed    