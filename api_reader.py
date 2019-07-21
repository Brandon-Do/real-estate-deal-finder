import requests
import json

class ApiReader:
    def send_post_request(self, api_url, params_dict):
        params = json.dumps(params_dict)
        return requests.post(api_url, params)

if __name__ == '__main__':
    pass