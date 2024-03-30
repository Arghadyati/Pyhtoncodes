#Abstraction

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("car started")

c1=Car()
c1.start()#here the information of acc and clutch is hiddden outside class that is abstraction