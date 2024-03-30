with open("practice.txt","r")as f:
    data=f.read()
    
newdata=data.replace("java","python")

with open("practice.txt","w")as f:
    f.write(newdata)
    