from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class StaffPermissionsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'staff_permissions'
    KEY_PROPERTIES = ['id']
    REQUIRES = ['staff']
    RESPONSE_KEY = 'StaffPermissions'
    IS_PAGINATED = False

        
    @property
    def path(self):
        return '/staff/staffpermissions'
        
    def get_params(self, staff_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'StaffId': staff_id
        }
        return params      
         
    def transform_stream_data(self, response):
        transformed = []
        record = self.transform_record(response) 
        transformed.append(record)
        return transformed
            
    def get_stream_data(self, url, params):
        table = self.TABLE
        LOGGER.info('Syncing data for {}'.format(table))
        
        try:
            response = self.client.make_request(url, self.API_METHOD, params)
            if response is None:
                return None, None
        except RuntimeError as e:
            if 'StaffMemberNotFound' in str(e):
                return None, None
            else:
                raise
                
        transformed = self.transform_stream_data(response)
        
        with singer.metrics.record_counter(endpoint=table) as counter:
            singer.write_records(table, transformed)
            counter.increment(len(transformed))
        
        return response, transformed
        