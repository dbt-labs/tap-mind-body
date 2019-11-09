from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class AcceptedCardTypesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'accepted_card_types'
    KEY_PROPERTIES = ['accepted_card_types']
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/sale/acceptedcardtypes'
    
    def transform_stream_data(self, response):
        transformed = []
        for record in response:
            record = self.transform_record({'accepted_card_types': record, 'Id': hash(record)}) 
            transformed.append(record)

        return transformed    