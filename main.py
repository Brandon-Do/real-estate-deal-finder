import data_access as da

def main():
    print('starting program')
    data_access = da.ZillowDataAccess()
    response = data_access.get_address_search_results('15403 SE Ivy Creek St.', '97086', True)
    print(response.text)

if __name__ == '__main__':
    main()
