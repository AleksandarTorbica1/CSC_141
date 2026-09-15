# Alex Torbica
# Chapter 3
# This program will print a list of countries and print the list in different orders.

countries = ["Serbia", "Mexico", "Sweden", "Norway", "Canada"]

print(countries)

countries.append("Iceland")
print(countries)

countries.insert(0, "Greenland")
print(countries)

del countries[1]
print(countries)

popped_country = countries.pop()
print(f"I removed {popped_country} from the list.")
print(countries)

print(sorted(countries))

countries.sort()
print(countries)

countries.reverse()
print(countries)

num_countries = len(countries)
print(f"There are {num_countries} countries in my list.")