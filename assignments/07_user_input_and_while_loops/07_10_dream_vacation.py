# Alex Torbica
# Chapter 7
# This command asks the user for their name and where they would like to go on vacation. Then it stores the responses in a dictionary with the empty responses command then quits the statement when response with no afterwards.

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")