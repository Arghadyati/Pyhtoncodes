# Dictionaries

dict = {
    "name": "argha",
    "cgpa": 8.9,
    "marks": [100, 70, 80]
}

null_dict = {}
print(null_dict)

print(type(dict))
print(dict)
print(dict["name"])
print(dict["marks"])
dict["name"] = "Arghadyati"
dict["surname"] = "Bayen"
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name2"))  # None -> if key is not present
dict.update({"city": "kolkata"})
print(dict)

# nested dictionary
student = {
    "name": "arghadyati",
    "subjects": {
        "chem": 80,
        "phy": 90,
        "math": 92
    }
}
print(student["subjects"]["phy"])
