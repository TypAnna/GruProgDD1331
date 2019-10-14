fibDictionary = {} #a dictionary
def niceFib(n):
    if n in fibDictionary:
        print(n, "in dictionary as", fibDictionary[n])
        return fibDictionary[n]
    elif n == 0 or n == 1:
        print("insert fib", n, "as 1")
        fibDictionary[n] = 1
        return 1

    else:
        fib =  niceFib(n-2) + niceFib(n-1)
        fibDictionary[n] = fib
        print("insert fib", n, "as", fib)
        return fib #this is a base case-ish. It is a base case because we return
                   #an actual value. The "ish" part comes from the fact that we
                   #get it from two recursive calls.

print(niceFib(7))
