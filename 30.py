# Multiple inheritence
class A:
    a = "Welcome to class A"


class B:
    b = "Welcome to class B"


class C(A, B):
    c = "welcome to class C"


c1 = C()
print(c1.a)
