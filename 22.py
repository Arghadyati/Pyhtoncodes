# class Student:
#     name="karan"

# s1=Student()#object(instance of class)
# print(s1.name)

# class Car:
#     color="blue"
#     brand="mersidise"

# car1=Car()
# print(car1.color)
# print(car1.brand)

class Student:
    collegename = "GMIT"  # class attribute

    def __init__(self, name, age, stream, marks):
        self.name = name
        self.age = age
        self.stream = stream
        self.marks = marks
        print("adding new student to our database....")


s1 = Student("arjun", 22, "E.C.E", 98)  # object instance 1
print(s1.name)
print(s1.age)
print(s1.stream)
print(s1.marks)
print(s1.collegename)

s2 = Student("karan", 22, "E.C.E", 95)  # object instance 2
print(s2.name)
print(s2.age)
print(s2.stream)
print(s2.marks)
print(s2.collegename)  # also valid Student.collegename
