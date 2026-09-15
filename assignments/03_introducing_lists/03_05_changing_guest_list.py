# Alex Torbica
# Chapter 3
# This program will print a list of guests and a message inviting them to dinner. It will also change one of the guests and print the new list of guests. And say someone cant make it to dinner.

guests=["Jimmy Fallon", "Bob Marley", "Charlie Damelio"]

print(f" Dear {guests[0]}, I am inviting you to my dinner tonight.")
print(f" Dear {guests[1]}, I am inviting you to my dinner tonight.")
print(f" Dear {guests[2]}, I am inviting you to my dinner tonight.")

print(f"Unfortunately {guests[1]} cant make it to the dinner tonight.") 

guests[1] = "Jack Ripper"

print(f"Dear {guests[0]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[1]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[2]}, I am inviting you to my dinner tonight.")
