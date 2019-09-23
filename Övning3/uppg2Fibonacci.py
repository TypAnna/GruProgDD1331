#Returns the nth fibonacci number.
def fibonacci(n):
    #the first two fibonacci numbers
    i = 1
    j = 1

    #calculate the next n-2 numbers
    for el in range(1, n-1): #we have already calculated the first two
        print(el)
        tmp = j
        j = i + j
        i = tmp

    return j #the return value is the ouput of the function


k = int(input("Give me a number: "))
fibNumber = fibonacci(k) #the return value from the function will be set to fibNumber
print("The", str(k)+"th fibonacci number is", fibNumber)
