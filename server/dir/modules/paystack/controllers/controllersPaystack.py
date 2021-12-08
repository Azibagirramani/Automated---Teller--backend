from ..helpers.helperPaystack import HelperPaystack

class PaystackController(HelperPaystack):

    def get_transactions(self):
        return super().get_transactions_helper()

    def get_settlements(self):
        return super().get_settlements_helper()