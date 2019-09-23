#Return the semi factorial of the integer n
def semiFakultet(n):
    total = n
    #we want to continue to add factors as long as the last term is equal to
    #or greater than one
    while n-2 >= 1:
        total*= n - 2
        n -= 2 #same as n = n - 2
    return total

print(semiFakultet(7))
