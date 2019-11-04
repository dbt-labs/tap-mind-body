from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ScheduleItemsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'schedule_items'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'StaffMembers'
    IS_PAGINATED = True
        
    @property
    def path(self):
        return '/appointment/scheduleitems'
