from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'classes'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Classes'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'Clients',
        'Staff',
        'Visits',
        'Location',
        'ClassDescription'
    ]

    @property
    def path(self):
        return '/class/classes'
        
    def get_params(self, offset_value=0, limit_value=200):
        last_modified_date = self.get_start_date()
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'LastModifiedDate': last_modified_date
        }
        return params    