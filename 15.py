# Loops in python
# i=1
# while i<=5:
#     print("arghadyati")
#     i+=1

# for i in range(5):
#     print("hello")
#     i+=1

# list=[1,2,3,4,5]
# for x in list:
#     print(x)
# ques1
i = 1
while i <= 100:
    print(i)
    i = i+1
# ques2
k = 100
while k >= 1:
    print(k)
    k -= 1
# ques3
n = 3
j = 1
while j <= 10:
    print(n*j)
    j += 1
# ques4
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
p = 0
while p < len(list):
    print(list[p])
    p += 1
# ques5
x = 36
k = 0
flag = False
while k < len(list):
    if (list[k] == x):
        print("Found at index", k)
    k += 1

# if(flag):
#     print("present inside the list")
# else:
#     print("not present inside the list")
