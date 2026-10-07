# Alex Torbica
# Chapter 6
# This program has a dictionary of rivers and the countries they run through and it prints out the river and country in the section they are in

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china', 
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe rivers in the dictionary are:")
for river in rivers.keys():
    print(f"{river.title()}")

print("\nThe countries in the dictionary are:")
for country in rivers.values():
    print(f"{country.title()}")