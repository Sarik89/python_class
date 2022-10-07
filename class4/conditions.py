# # Number1 = 10
# # Number2 = 7
# # if Number1 is Number2:
# #     print("They are equal")
# # else:
# #         print("They are not equal")
# # if Number1 is not Number2:
# #     print("They are not equal")
# # else:
# #     print("They are equal")    
# # in comparison
# HIDDEN_FRUIT = "kiwi"
# FRUIT_LIST1 = ["apple", "pear", "banana"]
# print(type(FRUIT_LIST1))
# FRUIT_LIST2 = ("mango","melon","kiwi")
# print(type(FRUIT_LIST2))
# FRUIT_LIST3 = {"peach","apricot","cherry"}
# print(type(FRUIT_LIST3))
# if HIDDEN_FRUIT in FRUIT_LIST1:
#     print("Hidden fruit is in list1")
# elif HIDDEN_FRUIT in FRUIT_LIST2:
#  print("Hidden fruit is in list2") 
# elif HIDDEN_FRUIT in FRUIT_LIST3:
#     print("Hidden fruit is in list3")   
# else:
#      print("Hidden fruit is not found")
while True:
    try:
        RESPONSE = int(input("when were you born?:"))
        
        
        if RESPONSE >= 2000 and RESPONSE <= 2022:
            print ("You were born in 21st century")
        elif RESPONSE >= 1900 and RESPONSE <= 1999:
            print("You were bor in 20th century") 
        elif RESPONSE == 1800 or RESPONSE <=1899 :
            print("You shouldnt be runnning this.")      
        else:
            print("PLEASE GIVE ME RIGHT NUMBER")
        break    
    except:
        print(" ERROR:Did you provide digit e.g 1") 
    
    if RESPONSE >= 2000 and RESPONSE <= 2022:
        print ("You were born in 21st century")
    elif RESPONSE >= 1900 and RESPONSE <= 1999:
        print("You were bor in 20th century") 
    elif RESPONSE == 1800 or RESPONSE <=1899 :
        print("You shouldnt be runnning this.")      
    else:
        print("PLEASE GIVE ME RIGHT NUMBER")
        
    except:
        print("Did you provide digit e.g 1") 

    #Command + ] move to the right
    #command + [ move to the left

            #test
ANSWER = "no"
while ANSWER != "yes":
  ANSWER = input("Are you crazy? ")
  if ANSWER == "yes":
    print("I knew that")