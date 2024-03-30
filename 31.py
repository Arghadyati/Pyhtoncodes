class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class Toyota(Car):
    def __init__(self, brand,type):
        self.brand = brand
        super().__init__(type)


t1=Toyota("Fortuner","electric")
print(t1.type)