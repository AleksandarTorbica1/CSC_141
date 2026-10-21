# Alex Torbica
# Chapter 7
# This program asks the user to input a number and checks if it is a multiple of 10 in an if else statement. It uses the modulus operator to determine if the remainder when dividing by 10 is zero, indicating if the number is a multiple of 10.

chosen_number = input("what is your chosen number? ")

yes_or_no = int(chosen_number) % 10

if yes_or_no == 0:
    print(f"{chosen_number} is a multiple of 10!")
else:
    print(f"{chosen_number} is not a multiple of 10!")