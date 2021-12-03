import base64
import requests

class HelperSplynx:

    api_key = "e3888e3e18508f5c961e59e079e83992"
    secret = "8cf2ee02dd12c4e62d38ee75f56c026b"
    base_url = "https://demo.splynx.com/api/2.0/admin"

    API_KEY = "6f18c5631e07995b7ca646af2d2587d5"
    SURL = "https://selfcare.dotmac.ng/api/2.0/admin"
    SECRET_KEY = "9f714dd1277224dcfb70ce976d16e60d"

    def __init__(self):
        pass

    # convert secret, api_key to base64 and return in a single string
    def get_base64_string(self) -> str:
        base64String = '{}:{}'.format(self.API_KEY, self.SECRET_KEY)
        encodedBase64String = base64String.encode('ascii')
        base64_byte = base64.b64encode(encodedBase64String)
        return base64_byte.decode("utf-8")

    def get_headers(self) -> dict:
        return {
            'Authorization': 'Basic {}'.format(self.get_base64_string()),
            'Content-Type': "application/json; charset=utf-8"
        }

    def request_get(self, url: str = "") -> list or dict:
        return requests.get("{}/{}".format(self.SURL, url), headers=self.get_headers())

    # get all splynx customers

    def get_splynx_customers(self) -> list:
        url = "customers/customer"
        response = self.request_get(url)
        return response.json()[:20]

    # get all splynx customer

    def get_splynx_customer(self, customer_id: str = "") -> list:
        url = "customers/{}".format(customer_id)
        response = self.request_get(url)
        return response.json()


