from data_processing import validate_quantity

# data_processing.py

def validate_phone_number(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    return False

def validate_payment_method(method):
    valid_methods = ["cash", "card", "upi", "netbanking"]
    return method.lower() in valid_methods

def validate_quantity(quantity):
    try:
        q = int(quantity)
        return q > 0
    except:
        return False

def format_address(address):
    return address.strip().title()

def validate_reservation_time(time_str):
    # you can make more advanced time validation here
    return bool(time_str)

def validate_number_of_guests(guests):
    try:
        g = int(guests)
        return 1 <= g <= 20
    except:
        return False
