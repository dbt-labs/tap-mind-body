from tap_mind_body.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class ClientFormulaNotesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'client_formula_notes'
    KEY_PROPERTIES = ['Id']
    REQUIRES = ['clients']
    RESPONSE_KEY = 'FormulaNotes'
    IS_PAGINATED = True

        
    @property
    def path(self):
        return '/client/clientformulanotes'
        
    def get_params(self, client_id, offset_value=0, limit_value=200):
        params = {
            'offset': offset_value,
            'limit': limit_value,
            'ClientID': client_id
        }
        return params       