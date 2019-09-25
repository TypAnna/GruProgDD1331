#Defines a car class
class Car: #always start your class with an uppercase letter!

    '''whenever we create a new instance of a car, this method will be called.
    this is called the constructor'''
    def __init__(self, color, brand, maxSpeed): #must be named __initt__
    #self is a reference to the current instance of the class
        self.color = color
        self.brand = brand
        self.maxSpeed = maxSpeed
        self.speed = 0 #when we create a new car, it is not moving

    '''the constructor defines what should be printed when we write print(bCar)
    where bCar is an instance of a car
    if we do not define this method, python will print something else'''
    def __str__(self):
        return self.color + " " +self.brand

    '''changes the speed of the car'''
    def changeSpeed(self, inputSpeed):
        if inputSpeed < 0:
            self.speed = 0
        elif inputSpeed > self.maxSpeed:
            self.speed = maxSpeed
        else:
            self.speed =inputSpeed


def main():
    #we create a new instance of a car
    aCar = Car("red", "Volvo", 150) #here the __init__ method is called

    print(aCar) #the __str__ method will be called in the background

    print("Initial speed of the car:", aCar.speed)
    aCar.changeSpeed(70)
    print("current speed of the car:", aCar.speed)

    #create another car
    bCar = Car("pink", "BMW", 170)
    print(bCar)

    '''bCar and aCar is independent of one another. They are two differet objects
    with of the same class, just as 3 and 4 are two different instances (objects)
    of the same class, int '''


main()
