class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        #("increase the pets energy by 25")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        #("increases the pet's energy by 5 & health by 10")
        return self

    def play(self):
        self.health += 5
        #("increases the pet's health by 5")
        return self

    def noise(self):
        # print("prints out the pet's sound")
        print("pet's sound:", "Wooowooowoooowwwwwwww")
        return self

    def display_health(self):
        print(f"Pet's Name: {self.name}, Health: %{self.health}, Enegery: %{self.energy}")
        return self

# instances:
Scooby = Pet("Scooby", "Dobber", "Jumps", 100, 90)
Scooby.play().eat().sleep().noise().display_health()


# .......................//..........................//.........................


class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        # ("walks the ninja's pet invoking the pet play() method")
        # print("walks the ninja's pet")
        self.pet.play()
        return self

    def feed(self):
        # ("feeds the ninja's pet invoking the pet eat() method")
        # print("feeds the ninja's pet")
        if len(self.pet_food) > 0:
            food = self.pet_food.pop(
            print(f"Feeding {self.pet.name} {food}!")
        else:
            print("Oh no!!! you need more pet food")
        return self

    def bathe(self):
        # ("cleans the ninja's pet invoking the pet noise() method")
        print("cleans the ninja's pet")
        self.noise()
        return self

# instances:
# amani = Ninja("Amani", "Mkamba",
# "Orieos", "Bones", "Scooby")
# amani.walk()



