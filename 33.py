# property method
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"


stu = Student(98, 97, 99)
print(stu.percentage)

stu.phy = 86
print(stu.percentage)
