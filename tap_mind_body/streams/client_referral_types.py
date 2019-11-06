from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClientReferralTypesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'client_referral_types'
    KEY_PROPERTIES = ['Id']
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/client/clientreferraltypes'
        
    def transform_stream_data(self, response):
        transformed = []
        for record in response['ReferralTypes']:
            record = self.transform_record({'client_referral_types': record}) 
            transformed.append(record)

        return transformed            