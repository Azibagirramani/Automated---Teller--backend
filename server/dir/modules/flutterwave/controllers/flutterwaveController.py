from ..helpers.helpersFlutterwave import HelperFlutterWave

class FlutterwaveController(HelperFlutterWave):
    def __init__(self):
        pass

    def get_flutterwave_transactions(self):
        return super().get_transactions()['data']

    def get_flutterwave_settlements(self):
        return super().get_settlements()