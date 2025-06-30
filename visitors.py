# Visitor class to represent the visitors in the park, with attributes like name and age.

class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self, animal):
        if animal.carnivore == True:
            print(
                f"{animal.name} is meat-eater and can be dangerous, so feeding is strictly prohibited.")

        elif animal.is_sleeping == True:
            print(f"{animal.name} is resting now, so come later to feed!")

        elif animal.energy >= 150:
            print(f"{animal.name} is full now, so no more treats, please!")

        # elif animal.energy >= 120 or animal.is_sleeping == True:
        #     print(f"{animal.name} is resting now, so no more treats, please!")

        else:
            animal.energy += 20
            print(f"{self.name} is feeding to {animal.name}")
            print(f"Now energy of {animal.name} is {animal.energy}.")
