from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClassesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'classes'
    KEY_PROPERTIES = ['id']
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