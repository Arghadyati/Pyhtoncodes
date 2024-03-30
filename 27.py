class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Arghadyati")
del s1
print(s1.name)
