import random #imports the random module which allows us to use predefined methods
import time #does the same with the time module

secondsToWait = random.randint(1, 10) #generates a random integer between 1 and 10
time.sleep(secondsToWait) #pauses the program for secondsToWait seconds

'''
time.perf_counter() gives the current time in seconds calculated from one (some) baseline.
This baseline is undefined, so only the difference between two calls is valid
(since they have the same base line.)
'''
currentTime = time.perf_counter() #the time right before the "pop up"
inp = input("press enter")
timeAtKeyPress = time.perf_counter() #the time right after the key press

reactionTime = timeAtKeyPress - currentTime
print("Reaction time was: " + str(reactionTime) + " seconds")
