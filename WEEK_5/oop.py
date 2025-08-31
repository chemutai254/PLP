# Activity 1 - Constructor, Inheritance, Polymorphism, and Encapsulation
class Utencils:
    # Constructor
    def __init__(self, color, material, capacity):
        self.color = color 
        self.material = material
        self.capacity = capacity

# Inheritance
class Spoon(Utencils):
    def __init__(self, color, material, capacity, size):
        super().__init__(color, material, capacity)
        self.size = size

spoon = Spoon("Silver", "Metal", "100ml", "Medium")
print(f"Spoon Properties: {spoon.color}, {spoon.material}, {spoon.capacity}, {spoon.size}") 

# Encapsulation
class Fork(Utencils):
    def __init__(self, color, material, capacity, prongs):
        super().__init__(color, material, capacity)
        self.__prongs = prongs  # Making the attribute private

    def get_prongs(self):
        print(f"Fork has {self.__prongs} prongs")

fork = Fork("Gold", "Metal", "150ml", 4)
fork.get_prongs()  # Accessing private attribute via method

# Polymorphism
class Knife:
    def sound(self):
        return "Slicing sound"

class Plate:
    def sound(self):
        return "Clinking sound"
    
for uten in [Knife(), Plate()]:
    print(uten.sound())

# Activity 2 - Polymorphism
class Car:
    def move(self):
        return "The car is driving"
class Boat:
    def move(self):
        return "The boat is sailing"
class Plane:
    def move(self):
        return "The plane is flying"
class Bicycle:
    def move(self):
        return "The bicycle is pedaling"
    
for vehicle in [Car(), Boat(), Plane()]:
    print(vehicle.move())
