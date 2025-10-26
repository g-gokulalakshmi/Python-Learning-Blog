class Animal:
    def make_sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows: Meow! Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()
