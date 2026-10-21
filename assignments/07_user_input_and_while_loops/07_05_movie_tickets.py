# Alex Torbica
# Chapter 7
# The command uses the if elif else statements to ask the user and go through their age and then checks to see the price of their ticket based on their age and will stop when typed "quit".

tickets = True
while tickets:
    age_of_person = input("What is your age? ")
    if age_of_person == 'quit':
        tickets = False
    elif int(age_of_person) < 3:
        print("Your ticket is free!")
    elif int(age_of_person) >= 3 and int(age_of_person) <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")