# Alex Torbica
# Chapter 6
# This program does the same as the previous section but prints outs a new key to add the total population of the cities combined in the dictionary

cities = {
    'philadelphia': {
        'country': 'United States',
        'population': 1584200,
        'fact': "Philadelphia is known for its rich history and is home to the Liberty Bell and Independence Hall."
    },

    'new york': {
        'country': 'United States',
        'population': 8419600,
        'fact': "New York City is the largest city in the United States."
    },

    'los angeles': {
        'country': 'United States',
        'population': 3980400,
        'fact': "Los Angeles is known for its entertainment industry, including Hollywood."
    }
}

total_population = 0

for city, info in cities.items():
    print(f"=={city.title()} ==")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    total_population += info['population']

print(f"\nTotal population of all cities: {total_population}")
