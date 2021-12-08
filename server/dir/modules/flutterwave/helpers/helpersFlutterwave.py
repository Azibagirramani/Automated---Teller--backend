from rave_python.rave_transfer import Transfer
import requests



class HelperFlutterWave(Transfer):

    baseUrl = "https://api.flutterwave.com/v3/"
    secret_key = "FLWSECK_TEST-8c5c4521f5cfc2029f387920ec1a1679-X"
    def __init__(self) -> None:
        pass
    
    def get_header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.secret_key)
        }

    def get_request(self, url):
        return requests.get( "{}{}".format(self.baseUrl, url), headers=self.get_header())
    
    def get_transactions(self, *data):
        urls = "transactions"

        response = self.get_request(urls)
        return response.json()


    def get_settlements(self, *data):
        urls = "settlements"

        response = self.get_request(urls)
        return response.json()