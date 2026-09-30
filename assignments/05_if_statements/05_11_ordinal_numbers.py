# Alex Torbica
# Chapter 5

# This prints out a if elif else chain inside a bracket loop with numbers starting from 1, 2, 3 going so forth to end in "th"

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
