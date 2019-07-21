import configparser as cp

class ConfigurationHandler:
    def __init__(self, file_name='credentials.ini'):
        self.config = {}
        self.read_credentials_from_file(file_name)

    def get_configuration_section(self, section_name):
        return self.config[section_name]

    def get_configuration_value(self, section_name, value_name):
        return self.config[section_name][value_name]

    def read_credentials_from_file(self, file_name):
        try:
            self.config = cp.ConfigParser()
            self.config.read(file_name)
        except:
            raise Exception('trying to read credentials from {} which does not exist.', file_name)

if __name__ == '__main__':
    pass