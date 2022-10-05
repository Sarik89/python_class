# Number1 = 10
# Number2 = 7
# if Number1 is Number2:
#     print("They are equal")
# else:
#         print("They are not equal")
# if Number1 is not Number2:
#     print("They are not equal")
# else:
#     print("They are equal")    
# in comparison
HIDDEN_FRUIT = "kiwi"
FRUIT_LIST1 = ["apple", "pear", "banana"]
print(type(FRUIT_LIST1))
FRUIT_LIST2 = ("mango","melon","kiwi")
print(type(FRUIT_LIST2))
FRUIT_LIST3 = {"peach","apricot","cherry"}
print(type(FRUIT_LIST3))
if HIDDEN_FRUIT in FRUIT_LIST1:
    print("Hidden fruit is in list1")
elif HIDDEN_FRUIT in FRUIT_LIST2:
 print("Hidden fruit is in list2") 
elif HIDDEN_FRUIT in FRUIT_LIST3:
    print("Hidden fruit is in list3")   
else:
     print("Hidden fruit is not found")
