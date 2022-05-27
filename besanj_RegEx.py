import re


def validate_email(email):
    if re.match(r'^[a-zA-Z\d\.\_]+@[a-zA-z\d]+\.[a-zA-Z]{3}$', email):
        return True
    else:
        return False


def validate_phone(number):
    if re.match(r'^09[\d]{9}$', number) or re.match(r'^\+989[\d]{9}$', number) or re.match(r'^00989[\d]{9}$', number):
        return True
    else:
        return False


"""
def validate_email(email):
    return bool(re.match(r"^[a-zA-Z1-9\.\_]+@[a-zA-Z1-9]+\.[a-zA-Z]{3}$", email))


def validate_phone(number):
    return bool(re.match(r"^(0|\+98|0098)9[0-9]{9}$", number))
"""

