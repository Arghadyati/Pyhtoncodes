#practice question
# movies=[]
# mov1=input("enter first movie : ")
# mov2=input("enter second movie : ")
# mov3=input("enter third movie : ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#question 2
list1=[1,2,3,2,1]
list2=list1.copy()
list1.reverse()
if(list1==list2):
    print("palindrome")
else:
    print("not palindrome")