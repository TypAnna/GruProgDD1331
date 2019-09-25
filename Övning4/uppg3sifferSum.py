#Calculates the number sum of an integer recursively
def sifferSum(tal):
    if tal // 10 == 0: #base case
        return tal

    return tal % 10 + sifferSum(tal // 10)
    #note that we dont have an else clause here - why is that?

print(sifferSum(12345))
