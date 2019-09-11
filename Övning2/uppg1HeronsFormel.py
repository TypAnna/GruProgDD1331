import sys
import math

#Calculates the area of a triangle using Herons formula.
def calculate_triangle_area(a, b, c):
    if a+b<c or a+c<b or b+c<a:
        print("You need to enter a valid triangle!")
        a = int(input("ge a"))
        # calculate_triangle_area()
        sys.exit() #closes the program
    #--------- end of if-statement ---------
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area is", area)
#---------- end of function definition ------

calculate_triangle_area(1, 2, 3) #call (run) the method
#when calling the method, a will be set to 3, b to 4 and c to 5
