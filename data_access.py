import configuration_handler as conf
import api_reader as api

class ZillowDataAccess:
    """ This class will handle the accessing of data to the Api """
    def __init__(self):
        config = conf.ConfigurationHandler().get_configuration_section('ZILLOW')
        self._zwid = config['zwid']
        self._api_base_url = config['api_url']
        self._api = api.ApiReader()

    def get_address_search_results(self, address, citystatezip, rentzestimate):
        """ Find property with specific address

        :param address:
            The address of the property to search. This string should be URL encoded.
        :param citystatezip:
            The city+state combination and/or ZIP code for which to search.
            This string should be URL encoded. Note that giving both city and state is required. Using just one will not work.
        :param include_zestimate:
	        Return Rent Zestimate information if available (boolean true/false, default: false)
        :return:
        """
        url = self._api_base_url + 'GetSearchResults.htm'
        search_body = {
            'zws-id' : self._zwid,
            'address' : address,
            'citystatezip' : citystatezip,
            'rentzestimate' : rentzestimate
        }
        return self._api.send_post_request(url, search_body)

    def get_estimate(self, zpid, rentzestimate):
        """ The GetZestimate API will only surface properties for which a Zestimate exists.

        :param zpid:
            Required: The Zillow Property ID for the property for which to obtain information. The parameter type is an integer.
        :param rentzestimate:
            Optional: Return Rent Zestimate information if available (boolean true/false, default: false)
        :return:
        """
        url = self._api_base_url + 'getZestimate.htm'

if __name__ == '__main__':
    pass