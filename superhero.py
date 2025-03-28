class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.__power_level = power_level        # (encapsulation)

    def introduce(self):
        print(f"I am {self.name}! (Secretly: {self._secret_identity})")

    def _show_power_level(self):  # Protected method
        print(f"Power level: {self.__power_level}")

    def use_power(self):
        raise NotImplementedError("Subclasses must implement this!")


# Inheritance: Hero and Villain are specialized Superheroes
class Hero(Superhero):
    def use_power(self):  # Polymorphism
        print(f"{self.name} uses their power for justice!")
        self._show_power_level()  # Accessing


class Villain(Superhero):
    def use_power(self):  # Polymorphism
        print(f"{self.name} unleashes chaos!")
        self._show_power_level()


# Encapsulation 
batman = Hero("Batman", "Bruce Wayne", 90)
joker = Villain("Joker", "???", 85)

batman.introduce()        
joker.introduce()         

batman.use_power()        
joker.use_power()         
