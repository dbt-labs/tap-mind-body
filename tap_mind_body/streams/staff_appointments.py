from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class StaffAppointmentsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'staff_appointments'
    KEY_PROPERTIES = ['id']
    IS_PAGINATED = True
    RESPONSE_KEY = 'Appointments'
        
    @property
    def path(self):
        return '/appointment/staffappointments'       