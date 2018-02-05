import re
import sys

def email_validation_check(email):
    """
    checking e-mail address validation

    Args : email (str) : e-mail address string

    Return : True or False (boolean) : the result of checking validation
    """

    if re.findall(r'[\w.-]+@[\w.-]+.\w+', email) [0] != email:
        print(email, "is incorrect e-mail type")
        return False

    print(email, 'is correct e-mail type')
    return True

    if __name__ = '__main__':
        email_validation_check(str(sys.argv[1]))
