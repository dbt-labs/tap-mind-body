from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class StaffStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'staff'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'StaffMembers'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'Appointments',
        'Availabilities',
        'Unavailabilities'
    ]

    @property
    def path(self):
        return '/staff/staff'
