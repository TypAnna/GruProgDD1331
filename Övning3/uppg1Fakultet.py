#Returns the facotorial of of the input n.
def fakultet(n):
    if n < 0:
        print("You need the pass a non-negative integer!")
        return #if we dont specify what we want to return, None (keyword) will be returned
        #the function will terminate as soon as it reaches a 'return'-statement
        #so we dont have to use sys.exit() which terminates the entire function!

    total = 1
    for i in range(1, n+1): #the upper bound of range() is exclusive
        total *= i
    return total #we can have multiple returns in one function

k = int(input("Give me an integer: ")) #thanks to 'return' we can save the result
answer = fakultet(k)
print("The factorial of", k, "is", answer) #calls and prints the factorial
