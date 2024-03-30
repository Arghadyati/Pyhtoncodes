#conditionals
light=input("light : ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")


if(light=="red" or light=="yellow" or light=="green"):
    print("valid color")
else:
    print("not a valid color")