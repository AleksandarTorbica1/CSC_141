# Alex Torbica
# Chapter 5

# Takes names from current and new users and programed loop through to print out each name with a statement wether it need a new username of is available

current_users = ['alex', 'admin', 'jake', 'adam', 'sam']
new_users = ['ALEX', 'joe', 'admin', 'timmy', 'kat']

current_users_lower = [user.lower() for user in current_users]

# Notice the lower command meaning the name alex in lowercase is still in the current users list making it print ALEX needs a new username

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: you will need to enter a new username.")
    else:
        print(f"{new_user}: that username is available.")