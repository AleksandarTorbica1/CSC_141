# Alex Torbica
# Chapter 6
# Whats created here is a dictionary that has the names of people and their favorite numbers. Then printed out using a for loop to print out the favorite numbers is seperate sentences

favorite_numbers = {
    'alex': 23,
    'joe': 7,
    'sam': 42,
    'luke': 1,
    'rick': 3
}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")