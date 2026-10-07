# Alex Torbica
# Chapter 6
# This program has a dictionary of people and their favorite places. And prints out each persons name in the for loop but then says the favorite place put in the bracket on the command

favorite_places = {
    'alex': ['philly', 'florida', 'arizona'],
    'joe': ['new york', 'california', 'texas'],
    'sam': ['washington', 'oregon', 'nevada'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")