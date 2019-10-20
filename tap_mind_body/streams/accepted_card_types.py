from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class AcceptedCardTypesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'accepted_card_types'
    KEY_PROPERTIES = ['id']
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/sale/acceptedcardtypes'

    def get_stream_data(self, response):
        transformed = []
        for record in response:
            #record = self.transform_record(record) 
            transformed.append(record)

        return transformed