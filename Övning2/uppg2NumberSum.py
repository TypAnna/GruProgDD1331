import sys

#Calculates the sum of the integers in a 3-digit number.
def calculate_number_sum_3(aNumber): #defines a method that takes a parameter
    if aNumber < 100 or aNumber > 999:
        print("The number must be 3 digits!")
        sys.exit() #closes the program
    #-------- end of if-statement------

    entalsSiffran = aNumber % 10

    rest = aNumber // 10 #floor division
    tiotalsSiffran = rest % 10

    rest = rest  // 10 #same as writing rest //= 10
    hundratalsSiffran = rest % 10

    total = entalsSiffran + tiotalsSiffran + hundratalsSiffran
    print("The number sum of", aNumber, "is", total)

#--------end of method--------

inputNumber = int(input("Give me a 3-digit number "))

calculate_number_sum_3(inputNumber)
#note the name of the input to the function does not have to be 'aNumber'
