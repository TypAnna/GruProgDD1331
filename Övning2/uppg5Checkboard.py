#Returns a string of representing an even row.
def even_row_string(size):
    evenRow = ""
    for col in range(size):
        if col % 2 == 0:
            evenRow += "*"
        else:
            evenRow += " "
    return evenRow

#Returns a string representing an odd row.
def odd_row_string(size):
    oddRow = ""
    for col in range(size):
        if col % 2 == 0:
            oddRow += " "
        else:
            oddRow += "*"
    return oddRow

#Prints a size*size checkerboard.
def checkerboard(size):
    evenRow = even_row_string(size) #create the even row once
    oddRow = odd_row_string(size) #do the same for odd rows
    for row in range(size):
        rowString = ""
        if row % 2 == 0:
            print(evenRow)
        else:
            print(oddRow)

checkerboard(5) #call (run) the method
