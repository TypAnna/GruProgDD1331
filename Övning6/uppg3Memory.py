def funB(t, a):
    t[1] = "hej"
    a[0][0] = ["wow"]

def funA():
    t = ([1, 2], "myra")
    a = [5, 6]
    funB(a, t)
    #what does the memory look like here?
    print("this is t", t)
    print("this is a", a)

funA()
