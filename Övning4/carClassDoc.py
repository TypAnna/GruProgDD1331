class Car:
    """
    A class used to represent a Car

    ...

    Attributes
    ----------
    color : str
        the color of the car
    brand : str
        the brand of the car
    maxSpeed : int
        the max speed of the car
    speed : int
        the current speed of the car

    Methods
    -------
    changeSpeed(inputSpeed)
        Changes the speed
    """

    def __init__(self, color, brand, maxSpeed):
        """
        Parameters
        ----------
        color : str
            the color of the car
        brand : str
            the brand of the car
        maxSpeed : int
            the max speed of the car
        """
        self.color = color
        self.brand = brand
        self.maxSpeed = maxSpeed
        self.speed = 0

    def __str__(self):
        return self.color + " " +self.brand


    def changeSpeed(intputSpeed):
        """Changes the speed of the car.

        Parameters
        ----------
        inputSpeed : int
            The speed of the car
        """
        if inputSpeed < 0:
            self.speed = inputSpeed
        elif inputSpeed > self.maxSpeed:
            self.speed = maxSpeed
        else:
            self.speed =inputSpeed
