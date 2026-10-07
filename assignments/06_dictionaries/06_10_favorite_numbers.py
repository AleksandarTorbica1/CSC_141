# Alex Torbica
# Chapter 6
# This one simply just adds another favorite number to each person in the dictionary and prints out all of the favorite numbers for each person
favorite_numbers = {
    'alex': {23, 2},
    'joe': {7, 5},
    'sam': {42, 24},
    'luke': {1, 8},
    'rick': {3, 9}
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")