#assigning a value of apple into a key "FRUIT"
FRUIT = "apple"
#Shows the value of the FRUIT key
print(FRUIT)
#shows the location of the string in the memory
print(id(FRUIT))
#shows the data type
print(type(FRUIT))
# #SHows the methods of the strings
# print(dir(FRUIT))
#capitalizes the first letter
print(FRUIT.capitalize())
#find how many times p repeated
print(FRUIT.count("p"))
#find out if the string starts with something
print(FRUIT.startswith("app"))
#Find out if the string end with something
print(FRUIT.endswith("pple"))
#change to uppercase
print(FRUIT.upper())
INCORRECT_STRING = "    spaced_string    "
#print value
print(INCORRECT_STRING)
#remove spacec on the left side
print(INCORRECT_STRING.lstrip())
#remove spaces on the right side
print(INCORRECT_STRING.rstrip())
#remove spaces from both sides
print(INCORRECT_STRING.strip())