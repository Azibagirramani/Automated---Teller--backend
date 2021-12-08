from ....configuration.database import Database


class HelperCustomer:

    Database = Database("customers")
    def __init__(self) -> None:
        pass 


    def getCustomers(self, data = {}) -> list or Exception:
        customers = []
        try:
            for x in self.Database.find(data):
                customers.append(x)
            return customers

        except Exception as e:
            print(e)
            return None

    # add to databse
    def addCustomer(self, data) -> bool or Exception:
        try:
            return self.Database.insert(data)
        except Exception as e:
            print(e)
            return False

    
    def updateCustomer(self, id, data) ->  bool or Exception:
        try:
            return self.Database.update(id, data)
        except Exception as e:
            print(e)
            return False

    # check if customer already exist using splynx is
    def checkCustomerBySplynxId(self, splynx_id: str) -> bool or Exception:
        try:
            return self.Database.find_one({"splynx": splynx_id})
        except Exception as e:
            print(e)
            return None


