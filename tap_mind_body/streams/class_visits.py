from tap_mind_body.streams.base import ChildStream
from tap_mind_body.streams.classes import ClassesStream
import singer

LOGGER = singer.get_logger()


class ClassVisitsStream(ChildStream):
    API_METHOD = 'GET'
    TABLE = 'class_visits'
    KEY_PROPERTIES = ['id']
    RESPONSE_KEY = 'Class'
    REQUIRES = ['classes']

    @property
    def path(self):
        return '/class/classvisits'

    def get_params(self, class_id):
        params = {
            'ClassID': class_id
        }
        return params

    def sync_data(self, parent=None):
        table = self.TABLE

        if parent is None:
            raise RuntimeError("Parent is required in substream {}".format(table))

        url = self.get_url()
        params = self.get_params(parent['Id'])

        LOGGER.info('Syncing data for {} for with params={}'.format(table, params))
        # Insert substream sync logic here
        #response = self.client.make_request(url, self.API_METHOD, params)
        #transformed = self.get_stream_data(response)
        #with singer.metrics.record_counter(endpoint=table) as counter:
        #    singer.write_records(table, transformed)
        #    counter.increment(len(transformed))
