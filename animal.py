class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.all_animals.append(self)

    def speak(self):
        print("The animal makes a noise.")

    def __str__(self):
        return f"Kingdom: '{Animal.kingdom}', Name: '{self.name}', Species: '{self.species}'"