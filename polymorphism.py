class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must define move()!")


class Car(Vehicle):
    def move(self):
        print("Driving on the highway!")


class Airplane(Vehicle):
    def move(self):
        print("Flying through the clouds!")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water!")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling down the street!")


class Rocket(Vehicle):
    def move(self):
        print("Blasting off into space!")



vehicles = [Car(), Airplane(), Boat(), Bicycle(), Rocket()]

print("=== How Vehicles Move ===")
for vehicle in vehicles:
    vehicle.move()  # 1 method different behaviors 
