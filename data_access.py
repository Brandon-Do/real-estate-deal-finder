import configuration_handler as ch

class ZillowDataAccess:
    """ This class will handle the accessing of data to the Api """
    def __init__(self):
        config = ch.ConfigurationHandler().get_configuration_section('ZILLOW')
        self.zwid = config['zwid']
        self.api_url = config['api_url']



if __name__ == '__main__':
    pass