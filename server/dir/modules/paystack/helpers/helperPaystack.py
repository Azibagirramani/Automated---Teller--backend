import requests

class HelperPaystack:


    baseUrl = "https://api.paystack.co/" 
    test_secret = "sk_test_20f5df27dd1b3f2ef630d361c637de355062df30"
    def __init__(self):
        pass


    def get_header(self):
        return {
            "Authorization": "Bearer " + self.get_paystack_secret(),
            "Content-Type": "application/json"
        }    
    
    def get_paystack_customers(self, url):
        pass

    def get_paystack_secret(self) -> str:
        return self.secret

    def get_paystack_url(self):
        return self.baseUrl

        
    def get_request(self, url) -> None or list:
        return requests.get("{}{}".format(self.baseUrl, url), headers=self.get_header())
    

    def get_transactions_helper(self):
        url = "transfer?page=1&perPage=10000000"
        response = self.get_request(url)
        return response.json()

    def get_settlements_helper(self):
        url = "settlement"
        response = self.get_request(url)
        return response.json()
