# Alex Torbica
# Chapter 7
# Same command as the previous section but includes a remove command to get rid of the pastrami orders from the list and prints a message that the pastrami is out of stock. Then it prints a loop of the rest of the sandwhiches that have been made as the result until all of the pastrami is removed.

sandwhich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwhiches = []

print("sorry, we are out of pastrami today.")

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print(f"I made your {current_sandwhich} sandwhich.")
    finished_sandwhiches.append(current_sandwhich)

print("\nThe following sandwhiches have been made:")
for sandwhich in finished_sandwhiches:
    print(sandwhich)
