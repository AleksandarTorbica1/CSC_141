# Alex Torbica
# Chapter 7
# These are three different exits statements that do the same as the previous code but in different ways, the first one is a while loop that checks if the age is not equal to quit, the second one is a while loop that checks if the active variable is true, and the third one is a while loop that checks if the age is equal to quit and breaks the loop if it is.

age = ""
while age != 'quit':
    age = input("What is your age? ")
    if age == 'quit':
        age =int(age)
        if age < 3:
            print("Your ticket is free!")
        elif int(age) < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

active = True
while active:
    age = input("What is your age? ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

while True:
    age = input("What is your age? ")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")