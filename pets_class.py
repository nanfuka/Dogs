class Dog:
    def __init__(self, name, age):
        self.is_hungry = False
        self.name = name
        self.age = age

    def eat(self):
        self.is_hungry = True


class Pets:
    dogs =[]
    species = 'mammal'
    def __init__(self, dogs):
        self.dogs = dogs
mypets = [Dog('Tom', 6), Dog('Fletcher', 7), Dog('Larry', 9)]       
      
pets = Pets(mypets)



print("I have {} dogs".format(len(pets.dogs)))

for dog in pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

    dog.eat()
x= False
for dog in pets.dogs:
    if dog.is_hungry:
        x=True
if x == False:
    print ("my dogs are hungry") 
else:
    print("my dogs are not hungry") 
