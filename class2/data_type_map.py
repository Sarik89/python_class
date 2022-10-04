person1 = {
    "firstname": "farrukh",
    "lastname": "sadykov",
    "address": "111 n state",
}
print(person1)
print(id(person1))
print(type(person1))
print(dir(person1))
print(person1.values())
print(person1.keys())
print("This person's firstname is",person1.get("firstname"))
print("This person's lastname is",person1.get("lastname"))
print("This person's address is",person1.get("address"))
