class Pets:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
pets = Pets('Tom', 6)
print("I have 3 dogs.")
print("{} is {}.".format(pets.name, pets.age))

pet = Pets('Fletcher', 7)
print("{} is {}.".format(pet.name, pets.age))

pet = Pets('Larry', 9)
print("{} is {}.".format(pet.name, pet.age))
print("And they're all {} of course.".format(pet.species))

class Dog(Pets):
    def __init__(self):
        self.is_hungry = True
    def eat(self):
        if self.is_hungry:
            return "My dogs are not hungry"
        return "My dogs are hungry"
    def walk(self):
        return "%s is walking!" % (self.name)
        
dog = Dog()
print(dog.walk())


        