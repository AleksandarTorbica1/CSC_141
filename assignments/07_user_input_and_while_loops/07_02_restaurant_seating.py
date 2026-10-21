# Alex Torbica
# Chapter 7
# Prints a command that asks a question in the terminal to allow the user to input how many people are in the group. Then checked with the if else statement to see if the table is ready by how many people are in the group

number_of_people = input("How many people are in your dinner group? ")

if int(number_of_people) > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")