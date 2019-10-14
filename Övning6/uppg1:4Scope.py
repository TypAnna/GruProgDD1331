'''do NOT confuse the previous examples with the following'''

animals = ["katt", "tiger"]

def my_function():
    print(animals) #prints the global variable 'animals'

    animals[1] = "myra" #we dont declare any new variable
    print(animals) #prints the altered (global) list

my_function()

'''print [katt, tiger] since we changed the list in our function'''
print(a)
