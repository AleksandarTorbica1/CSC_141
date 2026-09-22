# Alex Torbica
# Chapter 4

# My original pizzas
my_pizzas = ["pepperoni","chicken", "sausage"]

friend_pizzas = my_pizzas.copy()

# Inserting append command adds an item to list and pepperoni it is
my_pizzas.append("pepperoni")

friend_pizzas.append("ham")

# Overall prints both mine and my friends favorite pizzas
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)