from animal import Animal
from dog import Dog

if __name__ == "__main__":
    my_animal = Animal(name="Gerald-Herald", species="Lawn Gnome")
    print(my_animal)
    my_animal.speak()

    my_dog = Dog(name="Sir Fluffington", breed="Cavochon Hybrid")
    print(my_dog)
    my_dog.speak()

    print(Animal.all_animals)  # This will show all animals created, including the dog since it's a subclass of Animal
else:
    print("This code is meant to be run as a script, not imported as a module.")