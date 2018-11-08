class Pets:
    """initialise empty list"""
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

"""this is the parent class"""
class Dog:

    """initialise instance attributes"""
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        return "%s is walking!" % (self.name)

"""child class inheriting properties of Dog class"""
class Fletcher(Dog):
    pass

"""child class inheriting properties of Dog class"""
class Lary(Dog):
    pass

"""instance of dogs"""
mydog = [
    Lary("Tom"), 
    Fletcher("Fletcher"), 
    Dog("Larry")
]

pets = Pets(mydog)
pets.walk()


        