# int(..) converts the input to integers...
yearOfBirth = int(input("What year were you born? "))
currentYear = int(input("What year is it now? "))

# we need to do that in order to be able to subtract them
age = currentYear - yearOfBirth

# in order to print the age we need to convert it to a String with str(...)
# in python it makes no sense to add a string with an int. If we try to do that
# we will get a TypeError
print("You are roughly " + str(age) + " years old :-)")
