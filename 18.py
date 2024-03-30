# Recursion

def show(n):
    if (n == 0):
        return
    print(n, end=" ")
    show(n-1)


show(10)
print()


def front_printing(start, end):
    if (start > end):
        return
    print(start, end=" ")
    front_printing(start+1, end)


front_printing(1, 10)
print()


def fact(n):
    if (n <= 1):
        return 1
    return n*fact(n-1)


print(fact(10))


def calc_sum(n):
    if (n == 1):
        return 1
    return n+calc_sum(n-1)


print(calc_sum(10))

list=[1,2,3,4,5]

def print_list(idx,list):
    
    if(idx==len(list)):
        return
    print(list[idx])
    return print_list(idx+1,list)

print_list(0,list)