class TooBigNumError(Exception):
    def __init__ (self, val):
        self.val = val
    def __str__ (self):
        return 'Too big number {}. use 1~10!' .format(self.val)

def user_define_exception_test():
    num=int(input('input integer from 1 to 10 : '))
    if num >10:
        raise TooBigNumError(num)
    print("input number : {}".format(num))

user_define_exception_test()
