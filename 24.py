class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1+self.marks2+self.marks3)/3


s1 = Student("Argha", 95, 90, 80)
print(s1.average())
