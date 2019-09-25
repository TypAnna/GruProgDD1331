#recursive method that checks if a list is in increasing order
def isListIncreasing(aList):
    if len(aList) == 1: #base case
        #a list with one element is always in increasing order
        return True

    #check if the first two elements of the list are in order
    isFirstTwoInOrder = aList[0] <= aList[1]
    #and if the rest of the list (excluding the first element) is in order
    isRestOfListInOrder = isListIncreasing(aList[1:])
    return isFirstTwoInOrder and isRestOfListInOrder

bList = [1, 1, 2, 3, 9, 2, 3, 4]
print(isListIncreasing(bList))
