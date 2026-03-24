from animal import Animal
from dog import Dog
from cat import Cat

if __name__ == "__main__":
    my_animal = Animal(name="Gerald-Herald", species="Lawn Gnome")
    print(my_animal)
    my_animal.speak()

    my_dog = Dog(name="Sir Fluffington", breed="Cavochon Hybrid")
    print(my_dog)
    my_dog.speak()

    my_cat = Cat(name="Pityr", breed="Russian Blue")
    print(my_cat)
    my_cat.speak()

    print(Animal.all_animals)  # This will show all animals created, including the dog since it's a subclass of Animal
else:
    print("This code is meant to be run as a script, not imported as a module.")