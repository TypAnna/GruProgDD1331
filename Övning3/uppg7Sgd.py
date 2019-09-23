#Calculates the greates common divider of two integers
def gcd(a, b):
    #this is really just a translation of Euklides algorithm which you can find online
    while b != 0:
        rest = a % b
        a = b
        b = rest

    return a

print(gcd(15, 27))
print(gcd(5005, 9009))
