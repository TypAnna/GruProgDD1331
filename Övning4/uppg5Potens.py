#Calculates the power recursively
def power(base, exp):
    if exp == 0:
        return 1

    return base*power(base, exp-1)

print(power(2, 3))

#How many calls will this make to 'power'? Can we do it with fewer...?
