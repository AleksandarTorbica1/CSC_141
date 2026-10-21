# Alex Torbica
# Chapter 7
# This command creates a list of sandwhich orders and then uses a while loop to remove each order from the list and print a message that the sandwhich has been made. Then it prints a list of all the sandwhiches that have been made as the result.

sandwhich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwhiches = []

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print(f"I made your {current_sandwhich} sandwhich.")
    finished_sandwhiches.append(current_sandwhich)

print("\nThe following sandwhiches have been made:")
for sandwhich in finished_sandwhiches:
    print(sandwhich)
