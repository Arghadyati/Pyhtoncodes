def sum(a, b):
    return a+b


print(sum(10, 20))


def printhello():
    print("hello")


printhello()


def calc_avg(a, b, c):
    return (a+b+c)/3


print(calc_avg(20, 30, 40))

cities = ["delhi", "chennai", "mumbai", "kolkata", "bengalore"]


def print_list(list):
    for item in list:
        print(item, end=" ")  # to avoid next line printing


print_list(cities)
print()


def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i

    return ans


print(factorial(10))


def currency_converter(n):
    print("USD VALUE", n)
    print("INR VALUE", 83*n)


currency_converter(100)


def odd_even(n):
    if (n % 2 == 0):
        print("Even")
    else:
        print("Odd")


n = int(input("enter a number : "))
odd_even(n)
