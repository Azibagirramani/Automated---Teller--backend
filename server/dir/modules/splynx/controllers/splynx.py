from ..helpers.helperSplynx import *

class Splynx(HelperSplynx):
    
    # inherit all methods on super class
    def __init__(self) -> None:
        super().__init__()

    
    def get_customers(self) -> dict:
        """
        Get all customers from splynx
        """
        return self.get_splynx_customers()


    def get_transactions(self) -> dict:
        return self.get_splynx_transactions()

Splynx = Splynx()