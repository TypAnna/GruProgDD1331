#Calculates the number sum of a generic (positive) integer.
def calculate_general_number_sum(aNumber):
    total = 0
    for char in aNumber: #iterates over each character in the String (!) aNumber
        total += int(char)
    #-------- end of foor-loop --------

    print("The number sum of", aNumber, "is", total)
#--------- end of function ----------

inputNumber = input("Give me a integer ")
calculate_general_number_sum(inputNumber) #call (run) the method
