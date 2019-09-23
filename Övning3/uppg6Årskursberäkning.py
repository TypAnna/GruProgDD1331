CURRENT_YEAR = 19 #caps and underscore signals that this is a constant

def yearsAtKth(starYearString):
    startYear = int(starYearString[2:]) #takes everything except the first two characters
    if startYear >= 0 and startYear <= 19: #if person started this century
        years = CURRENT_YEAR - startYear
    else: #or the last one
        years = (100 - startYear) + CURRENT_YEAR
    #using return in yearsAtKth allows us to save the outcome
    return years

def main():
    someInput = "F-15"
    someYears = yearsAtKth(someInput)
    print("It has been", someYears, "since you started studying at KTH")
