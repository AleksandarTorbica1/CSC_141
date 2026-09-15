# Alex Torbica
# Chapter 3
# This program will print a list of guests and a message inviting them to dinner. It will also add more guests to the list on top of the old names and print the new list of guests.

guests=["Jimmy Fallon", "Bob Marley", "Charlie Damelio"]

print(f" Dear {guests[0]}, I am inviting you to my dinner tonight.")
print(f" Dear {guests[1]}, I am inviting you to my dinner tonight.")
print(f" Dear {guests[2]}, I am inviting you to my dinner tonight.")

print(f"Perfect news, I found a bigger table")

guests.insert(0, "Mo Bamba")
guests.insert(2, "Lebron Jimmy")
guests.append("Steph Curry")

print(f"Dear {guests[0]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[1]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[2]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[3]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[4]}, I am inviting you to my dinner tonight.")
print(f"Dear {guests[5]}, I am inviting you to my dinner tonight.")
