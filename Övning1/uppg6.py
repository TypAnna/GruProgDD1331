aliceFavAnimals = ["katt", "tiger", "lokatt"]
bobFavAnimals = ["katt", "tiger", "lokatt"]
# Alices and Bobs fave animals are the same, the object looks the same, but
# they are two DIFFERENT objects, pointing to different locations in the memory!
# They are completely independent of one another!!

print("Alices fave animals: " + str(aliceFavAnimals))
print("Bobs fave animals: " + str(bobFavAnimals))

print("Some years passes...")
aliceFavAnimals[0] = "hund"

print("Alices fave animals some years later: " + str(aliceFavAnimals))
print("Bobs fave animals: " + str(bobFavAnimals))
