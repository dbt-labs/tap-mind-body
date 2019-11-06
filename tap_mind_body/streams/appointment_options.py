from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class AppointmentOptionsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'appointment_options'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Options'
    IS_PAGINATED = False
        
    @property
    def path(self):
        return '/appointment/appointmentoptions'
