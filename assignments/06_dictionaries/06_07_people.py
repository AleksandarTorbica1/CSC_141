# Alex Torbica
# Chapter 6
# Programmed here is 3 different dictonaries of people with their first name, last name, age, and city. And prints out each single persons information as the for loop goes through all of them.

person_1 = {
    'first_name': 'Alex',
    'last_name': 'Torbica',
    'age': 19,
    'city': 'Philadelphia',
}

person_2 = {
    'first_name': 'Sam',
    'last_name': 'Smith',
    'age': 26,
    'city': 'New York',
}

person_3 = {
    'first_name': 'Chris',
    'last_name': 'Brown',
    'age': 45,
    'city': 'Jersey City',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Name: {full_name}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")