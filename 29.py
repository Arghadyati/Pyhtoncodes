# inheritence

class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type


car1 = Toyota("fortuner")
car2 = Toyota("prius")
car2.stop()
f1 = Fortuner("diesel")
f1.start()
