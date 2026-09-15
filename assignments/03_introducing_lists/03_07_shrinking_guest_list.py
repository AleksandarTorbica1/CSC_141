# Alex Torbica
# Chapter 3
# This program will print a list of guests invting them to dinner and saying there is a bigger table and more guests can be added to the list, but yet the table wont arrize in tiem so only can invite 2 people.

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

print("\nSorry, my new table won't arrive in time. I can only invite two people.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

print(f"\nDear {guests[0]}, you're still invited to dinner!")
print(f"Dear {guests[1]}, you're still invited to dinner!")

del guests[1]
del guests[0]

print(f"\nMy guest list is now: {guests}")