# Alex Torbica
# Chapter 5

# The same for loop program as the previous section but when the list of names is empty, its programed to print the else statement

usernames = ['alex', 'admin', 'jake', 'adam', 'sam']

for username in usernames:
    if username == 'admin':
        print("hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

else:
    print("we need to find some users")