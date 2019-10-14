def binomial(n, k):
    # print(n, k)
    if n == k: #how many ways can we pick k elemnts from k?
        return 1
    elif n == 0 or k == 0: #how many ways can we pick k elements from 0?
        return 1           #how many was can we pick 0 elements from n?
    elif k == 1: #how many ways can we pick 1 elements from n?
        return n
    elif n == 1: #how many ways can we pick k elements from 1? (k<n so k = 0 here)
        return 1
    else:
        return binomial(n-1, k-1) + binomial(n-1, k)

# print(binomial(25,8)) #how many times will this run? :0)



binDictionary = {}
def betterBinomial(n, k): #assumes OK values for n and k
    key = str(n)+":"+str(k)
    if key in binDictionary:
        return binDictionary[key]
    elif n == k:
        binDictionary[key] = 1
        return 1
    elif n == 0 or k == 0:
        binDictionary[key] = 1
        return 1
    elif k == 1:
        binDictionary[key] = 1
        return n
    else:
        binCoeff = betterBinomial(n-1, k-1) + betterBinomial(n-1, k)
        binDictionary[key] = binCoeff
        return binCoeff #this is a base case-ish. It is a base case because we return
                        #an actual value. The "ish" part comes from the fact that we
                        #get it from two recursive calls.


# print(betterBinomial(25, 8))
print(betterBinomial(6, 4))
print(betterBinomial(1, 1))
# print(betterBinomial(6, 2))







    #
    # if k > n or n < 0 or k < 0: #a bit unnecessary to have this in each run of func
    #     print("invalid params")
    #     return
