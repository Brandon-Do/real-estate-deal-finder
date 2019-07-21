import credential_handler as cred

def main():
    print('starting program')
    creds = cred.ConfigurationHandler()
    zwid = creds.get_configuration_value('ZILLOW', 'zwid')
    api_url = creds.get_configuration_value ('ZILLOW', 'api_url')
    print(zwid, api_url)

if __name__ == '__main__':
    main()
