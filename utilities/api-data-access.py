from configparser import ConfigParser

def connect_to_zillow_api():
    pass

def fetch_api_key():
    config = ConfigParser()
    return config['ZILLOW']['zwid']

if __name__ == '__main__':
    pass