import re 
def validate_username(username):
    if not username:
        return False
    if ' ' in username:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[a-zA-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def validate_email(email):
    if '@' not in email or '.' not in email:
        return False
    return True

def get_user_input():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    return username, email, password