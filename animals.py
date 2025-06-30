# Base class: Animal all types of animals
# Common attributes may include: name, age and energy level
# basic methods might be: eat, sleep, make sound.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100
        self.is_sleeping = False

    def eat(self):
        self.energy += 10
        print(f"{self.name} is eating.")

    def make_sound(self):
        print(f"{self.name} makes some sound.")

    def sleep(self):
        self.energy += 30
        self.is_sleeping = True
        print(
            f"{self.name} is sleeping now, recharging its energy to bring you joy later!")

    def energy_status(self):
        print(
            f"Animal name: {self.name}\nAge: {self.age}\nEnergy: {self.energy}")

# Subclass: Herbivores and carnivores that inherit from Animal, with specific characteristics and behaviors.


class Herbivores(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.carnivore = False

    def eat(self):
        self.energy += 40
        print(f"{self.name} eats only plant based food.")


class Carnivorous(Animal):
    def __init__(self, name, age, other_animal):
        super().__init__(name, age)
        self.other_animal = other_animal
        self.carnivore = True

    def eat(self):
        self.energy += 50
        print(f"{self.name} hunted {self.other_animal}")


class Lion(Carnivorous):
    def make_sound(self):
        print(f"{self.name} roars, giving visitors a thrilling scare!")


class Elephant(Herbivores):
    def make_sound(self):
        print(f"{self.name} trumpets, bringing smiles and laughter to our visitors!")


class Giraffe(Herbivores):
    def make_sound(self):
        print(f"{self.name} hums gently, delights nearby visitors!")
