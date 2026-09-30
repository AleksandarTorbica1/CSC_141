# Alex Torbica
# Chapter 5

# These are a series and different sets of more conditional tests that run true or false statements, upper or lowercase statements, and whether an item is in list or not and programed to answer each and every statement corectly

car = 'acura'

print("Is car == 'acura'? I predict True.")
print(car == 'acura')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("Is car != 'audi'? I predict True.")
print(car != 'audi')

print("Is car != 'acura'? I predict False.")
print(car != 'acura')

name = 'Ada'

print("Is name.lower() == 'ada'? I predict True.")
print(name.lower() == 'ada')
print("Is name.lower() == 'Ada'? I predict False.")
print(name.lower() == 'Ada') 

age = 21

print("Is age == 21? I predict True.")
print(age == 21)

print("Is age == 30? I predict False.")
print(age == 30)

print("Is age != 30? I predict True.")
print(age != 30)

print("Is age != 21? I predict False.")
print(age != 21)

print("Is age > 18? I predict True.")
print(age > 18)

print("Is age > 21? I predict False.")
print(age > 21)

print("Is age < 30? I predict True.")
print(age < 30)

print("Is age < 21? I predict False.")
print(age < 21)

print("Is age >= 21? I predict True.")
print(age >= 21)

print("Is age >= 22? I predict False.")
print(age >= 22)

print("Is age <= 21? I predict True.")
print(age <= 21)

print("Is age <= 20? I predict False.")
print(age <= 20)

age_0 = 22

age_1 = 18

print("Is age_0 >= 21 and age_1 >= 18? I predict True.")
print(age_0 >= 21 and age_1 >= 18)  

print("Is age_0 >= 21 and age_1 >= 21? I predict False.")
print(age_0 >= 21 and age_1 >= 21)   

print("Is age_0 >= 21 or age_1 >= 21? I predict True.")
print(age_0 >= 21 or age_1 >= 21)    

print("Is age_0 < 18 or age_1 < 18? I predict False.")
print(age_0 < 18 or age_1 < 18)      


pets = ['dog', 'cat', 'fish']

print("Is 'cat' in pets? I predict True.")
print('cat' in pets)

print("Is 'bird' in pets? I predict False.")
print('bird' in pets)

print("Is 'bird' not in pets? I predict True.")
print('bird' not in pets)

print("Is 'dog' not in pets? I predict False.")
print('dog' not in pets)