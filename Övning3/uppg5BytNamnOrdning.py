#Reverses the order of the first and last name
def bytNamnOrdning(name):
    nameList = name.split(" ") #we split the string where there is a blank space (" ")
    print(nameList[1], nameList[0])

bytNamnOrdning("hejsan svensson")
