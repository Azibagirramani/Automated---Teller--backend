import requests

class HelperPaystack:


    baseUrl = "https://api.paystack.co"
    secret = "sk_test_20f5df27dd1b3f2ef630d361c637de355062df30"

    def __init__(self):
        pass


    def get_header(self):
        return {
            "Authorization": "Bearer " + self.get_paystack_secret(self._secret),
            "Content-Type": "application/json"
        }    
    
    def get_paystack_customers(self, url):
        pass

    def get_paystack_secret(self, secret) -> str:
        return self._secret

    def get_paystack_url(self, url):
        return self._baseUrl

        
    def get_request(self) -> None or list:
        return requests.get(self.get_paystack_url(self._url), headers=self.get_header())
    

    def get_paystack_api_key(self, api_key):
        pass

