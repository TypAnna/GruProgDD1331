#Checks if a list contains duplicates.
def check_for_duplicates(aList):
    aList.sort() #sorts the list (and changes it!)
    for i in range(len(aList) - 1):
        if aList[i] == aList[i+1]:
            print("duplicate found!")
            break #exits the for-loop
        #--------- end of if-statement --------
    #----------- end of for-loop ------------
#--------- end of function definition -----

check_for_duplicates([1, 2, 4, 1, 1, 6, 2]) #run the method


inputList = input("Give me a list ").split(" ")
#.split(" ") splits a string and stores it in a list.
#" " is the delimiter where the string will be split
check_for_duplicates(inputList) #run it again
