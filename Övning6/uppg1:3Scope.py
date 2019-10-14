a = 0

def my_function():
    global a
    a = 3 #actually CHANGES the global variable a!!! BEWARE

    '''prints 3 to no ones suprise'''
    print(a)

my_function()

'''now this will print 3 since we wrtoe 'global' in our function'''
print(a)
