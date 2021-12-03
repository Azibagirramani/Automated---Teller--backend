from .base import *
from ...modules.customers.helpers.helperCustomers import HelperCustomer
from ...modules.splynx.helpers.helperSplynx import HelperSplynx
from fastapi import BackgroundTasks
import threading
import logging

class SyncSplynxCustomersWithLocal(BaseOperations, HelperCustomer, HelperSplynx):
    """
    Synchronise all splynx customers to local database
    """
    # database name

    Background_tasks = BackgroundTasks()

    def __init__(self) -> None:
        BaseOperations.__init__(self)
        HelperCustomer.__init__(self)
        HelperSplynx.__init__(self)

    # clean name remove mr, mrs., miss from string
    def clean_name(self, name: str) -> str:
        return name.replace("Mr.", "").replace("Mrs.", "").replace("Miss.", "").replace("Mr.", "").strip()


    # get first_name, last name from name
    def get_first_name_last_name(self, name: str) -> tuple:
        name = name.split(" ")
        if len(name) > 1:
            return name[0].capitalize(), name[1].capitalize()
        else:
            return name[0].capitalize(), ""
    
    # pick only one phone number if there are more than one
    def pick_phone_number(self, phone_numbers: str) -> str:
        phone_numbers = phone_numbers.split(",")
        if len(phone_numbers) > 1:
            return phone_numbers[0]
        else:
            return phone_numbers[0]

    # pick only one email if there are more than one
    def pick_email(self, emails: str) -> str:
        emails = emails.split(",")
        if len(emails) > 1:
            return emails[0]
        else:
            return emails[0]
    
    def SerilaizeData(self, data: dict) -> dict:
        return {
        'splynx': data['id'],
        'email': data['email'],
        'phone': data['phone'],
        'city': data['city'],
        'status': data['status'],
        'name': data['name'],
        'gps': data['gps'],
        "street_1": data['street_1'],

    } 

    # dump data to local database
    def dump_to_local(self, data: list = []) -> None:
        # customers to update   
        customers_to_update = []

        # customers to insert
        customers_to_insert = []

        # loop through data
        for current_cistomer in data:

            # serialize data
            data = self.SerilaizeData(current_cistomer)

            # format name 
            formattedName = self.clean_name(data['name'])

            # get first name and last name
            first_name, last_name = self.get_first_name_last_name(formattedName)

            # pick phone number
            phone = self.pick_phone_number(data['phone'])

            # pick email
            primaryEamil = self.pick_email(data['email'])

            customer_dict = {
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "email": primaryEamil,
                "city": data['city'],
                "status": data['status'],
                "splynx": data['splynx'],
                "gps": data['gps'],
                "street_1": data['street_1'],
            }

            # check if customer exists by splynx id
            customerOnDb = HelperCustomer().checkCustomerBySplynxId(data['splynx'])
            # if customer exists
            if customerOnDb:
                # query
                content = { "$set": customer_dict }
                # update customer
                HelperCustomer().updateCustomer({ "splynx": data['splynx']} , content)
                customers_to_update.append(customer_dict)
            else:
                # insert customer
                HelperCustomer().addCustomer(customer_dict)
                customers_to_insert.append(customer_dict)
        
    # return data summary for sync
            

    
    def sync(self) -> None:
        # create thread to sync
        sync_thread = threading.Thread(target=self.dump_to_local, args=(HelperSplynx().get_splynx_customers(), ))
        sync_thread.name = "sync_splynx_customers_with_local"
        self.Background_tasks.add_task(sync_thread.start())

        return "Synchronization started"


class SyncLocalCustomersWithPayStack(HelperCustomer):
    pass

SplynxCustomersWithLocal = SyncSplynxCustomersWithLocal()