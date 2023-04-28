import re

# Defining a function to check email validity
def is_valid_email(email):
    """Checks if an email address is valid"""
    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email, re.IGNORECASE):
        return True
    else:
        return False

# Examples for usage
if is_valid_email('shahzaib11@gmail.com'):
    print('Valid email')
else:
    print('Invalid email')
