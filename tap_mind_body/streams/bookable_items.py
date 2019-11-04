from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class BookableItemsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'bookable_items'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['session_types']
    IS_PAGINATED = True
    PARENT_ID = 'SessionTypeId'
    RESPONSE_KEY = 'Availabilities'
    FIELDS_TO_IGNORE = [
        'Staff',
        'Location'
    ]
        
    @property
    def path(self):
        return '/appointment/bookableitems'
        
    def get_params(self, session_type_id, offset_value=0, limit_value=200):
        last_modified_date = self.get_start_date()
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'SessionTypeIds': session_type_id
        }
        return params