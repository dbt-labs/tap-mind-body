from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class EnrollmentsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'enrollments'
    KEY_PROPERTIES = ['Id']
    RESPONSE_KEY = 'Enrollments'
    IS_PAGINATED = True
    FIELDS_TO_IGNORE = [
        'Classes',
        'Location',
        'Staff'
    ]

    @property
    def path(self):
        return '/enrollment/enrollments'
