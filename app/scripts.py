import phonenumbers
from email_validator import validate_email, EmailNotValidError
from dateutil import parser


def validate_phone_number(user_phone_number):

    try:
        phone_num = phonenumbers.parse(user_phone_number, "US")
        if phonenumbers.is_valid_number(phone_num):
            return True
        else:
            return False
    except:
        return False

def validate_email_address(user_email_address):
    try:
        check = validate_email(user_email_address, check_deliverability=True)
        user_email_address = check.normalized

    except EmailNotValidError as e:
        return False
    
    return True

def validate_each_input(list_of_inputs):
    for i in list_of_inputs:
        if str(i) == "" or str(i) == None:
            return False

    return True

def validate_date(user_date):
    try:
        if bool(parser.parse(user_date)) == True:
            return True
    except ValueError:
        return False
    
def validate_time(user_time):
    try:
        valid_zone = None
        valid_time = None
        
        if "AM" or "PM" in str(user_time).upper():
            valid_zone = True
        else:
            return False
        
        splitted_text = str(user_time).strip().split()
        
        if int(splitted_text[0].split(":")[0]) <= 12 and int(splitted_text[0].split(":")[0]) and int(splitted_text[0].split(":")[1]) <= 59 and int(splitted_text[0].split(":")[1]) >= 1:
            valid_time = True
        else:
            return False
        
        if valid_zone and valid_time:
            return True
    
    except ValueError:
        valid_zone = False
        valid_time = False
        return False

