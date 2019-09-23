import math

#Returns an approximatio of sin(x) using Taylor serier
def approxSin(x):
    sign = 1
    term = x
    div = 1
    total = x
    limit = 1e-10
    #continue adding terms as long as ther are big enough
    while abs(term) > limit:
        sign *= -1 #the sign alternates for each term
        term = term*x*x/((div+1)*(div+2))
        total += sign*term
        div += 2

    return total

def main():
    x = float(input("give x: "))
    print("approximation of sin", x, "is", approxSin(x))
    print("exact value is:", math.sin(x))

main()


















def approximate_sin(x):
    sign = 1
    exponent = 1
    total = x
    for i in range(10):
        sign *= -1 #the sign alternates betwwen 1 and -1
        exponent += 2 #the exponent increases with 2 for each term
        total += (sign*x**exponent)/fakultet(exponent)
        print(fakultet(exponent))
        print(sign*x**exponent)

    return total
