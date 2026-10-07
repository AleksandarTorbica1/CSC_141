# Alex Torbica
# Chapter 6
# This program does the same exact thing as the previous one but printts out a loop of each individual owner and their pets names seperate from each other

pet_1 ={
    'name': 'Buddy',
    'owner': 'Alex',
}

pet_2 = {
    'name': 'Max',
    'owner': 'Sam',
}

pet_3 = {
    'name': 'Bella',
    'owner': 'Chris',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Pet Name: {pet['name']}")
    print(f"Owner: {pet['owner']}\n")