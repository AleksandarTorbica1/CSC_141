# Alex Torbica
# Chapter 6
# This program has a dictionary of favorite programming languages and a list of people to poll. It checks if each person has taken the poll and prints a message specifically to it.

favorite_langauges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'alex': 'python',
}

people = ['joe', 'pete', 'john', 'sarah', 'alex']

for person in people:
    if person in favorite_langauges:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")