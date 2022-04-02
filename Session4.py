# Session 4 Prompt

# Write a Python program that declares a class describing 
# your favorite animal. Have the data members of the class 
# represent the following physical parameters of the animal: 
# length of the arms (float), length of the legs (float), 
# number of eyes (int), does it have a tail? (bool), is it 
# furry? (bool). Write an initialization function that sets 
# the values of the data members when an instance of the 
# class is created. Write a member function of the class to 
# print out and describe the data members representing the 
# physical characteristics of the animal.


class FavAnimal(): # do some math
    def __init__(self, armLen, legLen, numEyes, tail, furry):
        # Force cast types to what was requested
        self.armLen = float(armLen)
        self.legLen = float(legLen)
        self.numEyes = int(numEyes)
        self.tail = bool(tail)
        self.furry = bool(furry)

    def printParameters(self):
        print("\nCharacteristics of Animal")
        print("Arm Length: ", self.armLen)
        print("Leg Length: ", self.legLen)
        print("Number of Eyes: ", self.numEyes)
        print("Is there a Tail (T/F)? ", self.tail)
        print("Is it Furry (T/F)? ", self.furry)


def main(): # main function
    # When you dont know this about yourself let alone a fav animal
    animal = FavAnimal(True, 3.3, 2, True, False)
    # Who knows if those nums be milli, centi, inches, feet or miles lol
    animal.printParameters()

if __name__ == "__main__":
    main()