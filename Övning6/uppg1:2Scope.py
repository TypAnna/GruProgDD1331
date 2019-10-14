a = 0

def my_function():
    '''this will result in an error because when we refer to a global
    and local variable by the same name in the same function, the local will
    take prescidence...'''

    '''... so will try to print the local variable a - which has not yet been assgined!'''
    print(a)

    a = 3
    print(a)

my_function()

print(a)
