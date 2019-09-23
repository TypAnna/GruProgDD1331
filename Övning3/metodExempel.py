# name = "Abba" #these constants would be global
# age = 72

def sayHi(name, x):
    age = x + 10
    print("Hi " + name +", in 10 years you will be", age, "years old." )
    #this x, name, and age only lives inside this function!

def main():
    #all of these three work!

    sayHi("Steffe", 60)

    aName = "Annie"
    anAge = 35
    sayHi(aName, anAge)

    name="Jonas"
    age=56
    sayHi(name, age)

    #this aName, anAge, name, and age only lives inside this function!

main()
