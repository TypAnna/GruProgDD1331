'''Okay so if I have time (I don't think I will ;_;) I will update with more
comments explaining what is going on and why this works - but in the meantime
it's a great exercise to think about and draw what happens step by step when
we call the method with some list, say [1, 2, 3]
'''

#Returns all permutations of a list
def permutationOfList(aList):
    if len(aList) == 1 #base case
        return aList

    res = []
    print(aList)

    for i in range(0, len(aList)):
        curEl = aList[i]
        prt1 = aList[:i] #the left part
        prt2 = aList[i+1:] #the right part
        curList = prt1 + prt2
        for perm in permutationOfList(curList):
            if isinstance(perm, list):
                res.append(perm + [curEl])
            else:
                res.append([perm] + [curEl])


    return res

someList = [1, 2, 3]
perms = permutationOfList(someList)
print("The permutations of", someList, "is",perms)
print("The number of permutations are", len(perms))

'''Practice by drawing what happens in the computer, step by step!'''
