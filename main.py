from animals import Lion, Elephant, Giraffe
from visitors import Visitor


def simulate_zoo():
    # Creatting animals objects:
    lion = Lion("King", 15, "Rabbit")
    elephant = Elephant("Ellie", 25)
    girafee = Giraffe("Geo", 35)

    # Creatting visitors objects:
    visitor1 = Visitor("John", 30)
    visitor2 = Visitor("Kia", 12)

    print("🦒 🦁 🦣  Welcome to the Happy Tails Zoo. 🦣  🦁 🦒\n")

    # Animals natural routines:
    for animal in [lion, elephant, girafee]:
        animal.energy_status()
        animal.make_sound()
        animal.eat()
        # animal.sleep()
        print("\n")

    # Animals interaction with visitors:
    visitor1.feed_animal(elephant)
    visitor2.feed_animal(girafee)
    visitor2.feed_animal(elephant)
    elephant.sleep()
    visitor1.feed_animal(elephant)
    visitor1.feed_animal(lion)


if __name__ == "__main__":
    simulate_zoo()
