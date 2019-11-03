from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class WaitlistEntriesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'waitlist_entries'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['classes']
    RESPONSE_KEY = 'WaitlistEntries'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/class/waitlistentries'
        
    def get_params(self, class_id, offset_value=0, limit_value=10):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClassIDs': class_id
        }
        return params
  