#Example 1
aliceFavAnimals = ["katt", "tiger", "lokatt"]
bobFavAnimals = aliceFavAnimals #bob have the same favorite animals

#some time passes and alices favorite animals change (bobs still loves cats tho!)...
aliceFavAnimals[0] = "hund"
#aliceFavAnimals is now ["hund", "tiger", "lokatt"]

print("Alices favorite animals are: " + str(aliceFavAnimals))
print("Bobs favorite animals are: " + str(bobFavAnimals))

'''
Bobs favorite animals have changed aswell... why!?
Because on line 2 we do NOT make a copy of the list, we instead let bobFavAnimals
point to the SAME object as aliceFavAnimals! So when we change the list that
represent alices favorite animals, we also change bobs list (since they are one
and the same list)!
'''

print("--------------------")

#Example 2
#We follow the same example as above.
x = 5 #We declare one variable (x)...
y = x #... and then say that another variable (y) should be the same as x.
x = 4
print("x: " + str(x)) #prints x: 4
print("y: " + str(y)) #prints y: 5

'''
Here we get a different result! x and y are not the same. Why!?
Because x (and y) are of type integer, while aliceFavAnimals (and bobs)
are of type list.

Integer objects are IMMUTABLE, which means that they cannot be changed. When we
write x = 4 we create a NEW object (of type integer)!

Lists are instead MUTABLE. So when we write aliceFavAnimals[0] = "hund" we do
NOT create a new array object, we instead alter the existing one!

(More on this topic in Övning 2...)
'''
