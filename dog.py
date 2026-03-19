from animal import Animal
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    def __init__(self, name, species="Dog", breed=None):
        self.breed = breed
        super().__init__(name, species)
    
    def speak(self):
        print("The dog barks.")

    def __str__(self):
        return f"Kingdom: '{super().kingdom}', Name: '{self.name}', Species: '{self.species}', Breed: '{self.breed}'"