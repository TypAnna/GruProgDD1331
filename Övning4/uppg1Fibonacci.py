#Calculates the n:th fibonacci number recursively
def fibonacci(n):
    #basfall
    if n <= 2:
        return 1
    else:
    return fibonacci(n-1) + fibonacci(n-2)

k = 5
print("the", k, "fibonacci number is", fibonacci(k))

#what happens if we use a large k? try it yourself..
