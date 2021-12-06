from ..helpers.helperCustomers import HelperCustomer
from datetime import datetime
class ControllerCustomer(HelperCustomer):

    def __init__(self):
        super().__init__()


    # customer serializer
    def customerSerializer(self, items: dict) -> dict:
        return {
            'id': str(items['_id']),
            'first_name': items['first_name'],
            'last_name': items['last_name'],
            'phone': items['phone'],
            'email': items['email'],
            'city': items['city'],
            'status': items['status'],
            'billing_type': items['billing_type'],
            'date_add': items['date_add'],
            'last_online': items['last_online'],
            'last_update': items['last_update'],
        }

    def controllerGetCustomers(self):
        customerList = []
        for x in self.getCustomers():
            customerList.append(self.customerSerializer(items=x))

        return customerList


    def controllerCustomerFilter(self, *data):

        currentYear = datetime.now().year
        currentMonth = datetime.now().month
        currentDay = datetime.now().day
        dateTime = "{}-{}-{}".format(currentYear, currentMonth, currentDay)

        queryStack = []
        # # filter customer 
        customers = []
        # # get user by add_date
        if data[0]:
            queryStack.append({'date_add': {'$gte': data[0]}})

        if data[1]:
            queryStack.append({'status': data[1].lower()})


        if data[2]:
            queryStack.append({'last_update': {'$gte': data[2]}})


        if data[3]:
            queryStack.append({'billing_type': { '$regex': data[3].lower() }})

        if data[4]:
            queryStack.append({'first_name': {'$regex': data[4], '$options': 'i'}})
        
        finalQuery = {'$and': queryStack}

        for x in self.getCustomers(data=finalQuery):
            customers.append(self.customerSerializer(items=x))
    
        return customers

        # get current year, data, month

        # if data[0] > dateTime:
        #     print("dateTime: {}".format(dateTime))
