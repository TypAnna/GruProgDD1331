def funB(a, b):
	a[1]= "hej"
	b = ("katt", "lo")

def funA():
    a = [[1, 2], [3, 4]]
    b = (5, 6)
    funB(a, b)
    #what does the memory look like here?
    print("this is p", a)
    print("this is q", b)

funA()
