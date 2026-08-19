
class Car:
    def start():
        print("Car Started")

    def stop():
        print("Car Stopped")


class Toyota(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyota("Fortuner")
print(car1.name)  # Fortuner

car1.start()  # Car Started --> This is where Inheritance applied.