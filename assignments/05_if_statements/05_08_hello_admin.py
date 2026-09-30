# Alex Torbica
# Chapter 5

# Testing out a list of names in the bracket and creating for loop command of the names and creating the special greet for each person

usernames = ['alex', 'admin', 'jake', 'adam', 'sam']

for username in usernames:
    if username == 'admin':
        print("hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
        

