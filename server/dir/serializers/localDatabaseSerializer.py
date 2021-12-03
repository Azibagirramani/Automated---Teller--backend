

# filter data 
def CustomerLocalDatabaeSchema(data):
    return {
        'splynx': data['id'],
        'billing_email': data['billing_email'],
        'phone': data['phone'],
        'city': data['city'],
        'status': data['status'],
        'gps': data['gps'],
    }