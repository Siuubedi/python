class Car:
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")


class Toyota(Car):
    def __init__(self, name):
        self.name = name

    def toy_start(self):
        print("Toyota Started")


class Fortuner(Toyota):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type


car1 = Fortuner("Diesel")
print(car1.fuel_type)  # Diesel
print(car1.toy_start())  # Toyota Started
# Car Started. --> This used multi-level inheritace. Here, the start() method is from the Car class which is the parent of Toyota class, which is the parent of Fortuner class.
print(car1.start())