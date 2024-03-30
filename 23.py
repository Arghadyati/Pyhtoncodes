# methods in pyhton

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def printname(self):
        print(self.name)

    def get_marks(self):
        return self.marks


s1 = Student("arjun", 90)
s1.printname()
print(s1.get_marks())
