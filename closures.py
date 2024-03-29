"""closures"""
# outer function
# def add_ten():
#     ten = 10
#     # inner function
#     def add(num):
#         return num + ten
#     return add
#
# closure_result = add_ten()
# print(closure_result(5))
# print(closure_result(10))


"""Decorator"""

# outer function
def uppercase_decoration(function):
    def wrapper(): # inner function
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# reference function that called by the inner function of the uppercase_decoration which is outer function
@uppercase_decoration # annotation and giveing reference of main funciton using @ symbol to call directly our reference function
def greeting():
    return 'Welcome to Python'
print(greeting())
