# Define a clas for Animals
class Animal:
    def __init__(self, name, species, location):
        self.name = name
        self.species = species
        self.location = location

    # Define a function to move animals
    def move(self, new_location):
        print(f"{self.name} has moved from {self.location} to {new_location}")
        self.location = new_location

# Define a function to maintain wildlife
class WildlifeManagement:
    def __init__(self):
        self.animals = []

    # Define a function to add animals
    def add_animal(self, animal):
        self.animals.append(animal)

    # Define a function to remove animals
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    # Define a function to move all animals
    def move_all_animals(self, new_location):
        for animal in self.animals:
            animal.move(new_location)


# Example for usage
hawk = Animal("Shahzaib","Hawk","Alaska")
lion = Animal("Simba", "Lion", "Savannah")
Tiger = Animal("Sher Khan","Tiger","Amazon")
elephant = Animal("Dumbo", "Elephant", "Jungle")

manager = WildlifeManagement()
manager.add_animal(lion)
manager.add_animal(elephant)

manager.move_all_animals("Forest")
