class Dog:
    def say(self):
        print("hau")


class Cat:
    def say(self):
        print("meow")


pet = Dog()
pet.say()  # prints "hau"
another_pet = Cat()
another_pet.say()  # prints "meow"
lists = [1, 2, 3, 4, 5]
my_pets = [pet, another_pet]
for a_pet in my_pets:
    a_pet.say()
