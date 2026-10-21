# Alex Torbica
# Chapter 7
# This program is designed to allow the user to include an pizza toppings they want with the input command and will continue to ask the user until typed "quit" to stop the program.

pizzas = True
while pizzas:
    topping = input("What topping would you like on your pizza? ")
    if topping == 'quit':
        pizzas = False
    else:
        print(f"{topping} has been added to your pizza!")