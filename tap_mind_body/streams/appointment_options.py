from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class AppointmentOptionsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'appointment_options'
    KEY_PROPERTIES = ['Id']
    IS_PAGINATED = False
        
    @property
    def path(self):
        return '/appointment/appointmentoptions'

    def transform_stream_data(self, response):
        transformed = []
        for record in response['Options']:
            pk = hash(record.get('Name'))
            LOGGER.info('the pk is {}'.format(pk))
            LOGGER.info('the record is {}'.format(record))
            
            record.update({'Id': pk})
            LOGGER.info('the updated record is {}'.format(record))
            new_record = self.transform_record(record) 
            transformed.append(new_record)

        return transformed    