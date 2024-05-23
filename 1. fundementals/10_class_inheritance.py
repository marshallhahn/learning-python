class Mammal:
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        print(f"{self.name} can walk")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} says woof!")


class Cat(Mammal):
    def meow(self):
        print(f"{self.name} says meow!")


gizmo = Cat("Gizmo")
gilly = Cat("Gilly")
banjo = Dog("Banjo")

# Shared
gizmo.walk()
banjo.walk()

# Unique
gizmo.meow()
banjo.bark()
