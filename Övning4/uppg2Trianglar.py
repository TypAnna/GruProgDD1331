#Draws a triangle with its broadest part at the top
def triangelBasUpp(dist, bredd):
    #bredd is the number of stars on the base of the triangle
    #distance is number of blank spaces in the beginning of the row
    if bredd == 1: #base case
        print(dist*" " + "*")
    else:
        #if we are on on the base case, we want to print the current row
        #and THEN do the recursive call (since the triangle is the broadest
        #at the beginning)
        print(dist*" " + bredd*"*")
        triangelBasUpp(dist+1, bredd-2)

# triangelBasUpp(1, 5)


#Draws a triangle with its narrowest part at the top
def triangelBasNer(dist, bredd):
    if bredd == 1: #base case
        print(dist*" " + "*")
    else:
        #if we are on on the base case, we want do the recursive call (since the
        #triangle is the narrowest at the beginning) and THEN print the current
        #row
        triangelBasNer(dist+1, bredd-2)
        print(dist*" " + bredd*"*")




triangelBasNer(1, 5)
