'''what will be printed when we run this program?'''
a = 0 #this is a global variable

def my_function():
    a = 3 #a NEW local variable called 'a' is created and assigned value 3

    '''3 will be printed because if a local variable has the same name as
    a global variable, the local one will always take precedence'''
    print(a)

my_function()

'''this will print the global variable a with value 0 since it was never altered'''
print(a)
