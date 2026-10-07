# Alex Torbica
# Chapter 6
# The command here has a dictionary with different places as keys and includes the values of the city to each section of the dictionary. Then prints out a command for each of the cities information separately

cities = {
    'philadelphia': {
        'country': 'United States',
        'population': 1584200,
        'fact': "Philadelphia is home to the Liberty Bell."
    },

    'new york': {
        'country': 'United States',
        'population': 8419600,
        'fact': "New York City is the largest city in the United States and is known for its iconic landmarks such as Times Square."
    },

    'los angeles': {
        'country': 'United States',
        'population': 3980400,
        'fact': "Los Angeles is known for its entertainment industry, including Hollywood."
    }
}

total_population = 0

for city, info in cities.items():
    total_population += info['population']
    print(f"=={city.title()}==")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()