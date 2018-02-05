import sys

def password_validation_check(pwd):
    """ checking password validation

    Args:
        pwd (str) : password string

    Return :
        True or False (boolean) : the result of checking validation
    """
    if len(pwd) < 6 or len(pwd) >12:
        print(pwd, 'have length problem')
        return False

    for x in pwd:
        if not x.isnumeric() and not x.isalpha():
            print(pwd, 'dont consist of english and number')
            return False

    upper = False
    lower = False

    for x in pwd:
        if upper and lower:
            break

        if x.isalpha():
            if not upper:
                upper = x.isupper()
            if not lower:
                lower = x.islower()

    if not upper or not lower:
        print(pwd, 'dont have together upper and lower')
        return False

    print(pwd, 'is correct password')
    return True

    if __name__ == '__main__':
        password_validation_check(str(sys.argv[1]))
