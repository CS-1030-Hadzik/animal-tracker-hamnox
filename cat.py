from animal import Animal
class Cat(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    def __init__(self, name, species="Cat", breed=None):
        self.breed = breed
        super().__init__(name, species)
    
    def speak(self):
        print("The cat meows.")

    def __str__(self):
        if self.breed:
            return f"Kingdom: '{super().kingdom}', Name: '{self.name}', Species: '{self.species}', Breed: '{self.breed}'"
        return f"Kingdom: '{super().kingdom}', Name: '{self.name}', Species: '{self.species}'"