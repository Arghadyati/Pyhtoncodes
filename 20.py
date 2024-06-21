# writing to file
import os
f = open("demo.txt", "w")

f.write("i want to become a software engineer ")

f.close()

f = open("demo.txt", "a")

f.write("in tata consultancy services")

f.close()

f = open("sample.txt", "a")

f.close()

with open("sample.txt","r") as f:
    print(f.read())
    #we don't need to worry about closing the ffile using with syntax

os.remove("sample.txt")
