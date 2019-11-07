import requests
import singer
import singer.metrics

LOGGER = singer.get_logger()

    
class MindBodyClient:

    MAX_TRIES = 5

    def __init__(self, config):
        self.config = config
        
    def get_auth_token(self):
        response = requests.request(
            method='POST',
            url='https://api.mindbodyonline.com/public/v6/usertoken/issue',
            headers={
                'Content-Type': 'application/json',
                'API-Key': self.config['api_key'],
                'SiteId': self.config['site_id']
            },
            params=None,
            json={
                'Username': self.config['user_name'],
                'Password': self.config['password']
            }
        )
            
        if response.status_code != 200:
            LOGGER.info('status={}'.format(response.status_code))
            raise RuntimeError(response.text)

        raw_response = response.json()
        auth_token = raw_response.get('AccessToken')
            
        return auth_token    

    def make_request(self, url, method, params=None, body=None):
        LOGGER.info("Making {} request to {} ({})".format(method, url, params))

        response = requests.request(
            method,
            url,
            
            headers={
                'Content-Type': 'application/json',
                'API-Key': self.config['api_key'],
                'SiteId': self.config['site_id'],
                'Authorization': self.get_auth_token()
            },
            params=params,
            json=body)

        if response.status_code != 200:
            LOGGER.info('status={}'.format(response.status_code))
            raise RuntimeError(response.text)

        return response.json()

