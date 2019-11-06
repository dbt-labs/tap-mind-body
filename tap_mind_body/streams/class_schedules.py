from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassSchedulesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'class_schedules'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'ClassSchedules'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'Classes',
        'Staff',
        'Location'
    ]
        
    @property
    def path(self):
        return '/class/classschedules'
