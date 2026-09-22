# Alex Torbica
# Chapter 4

foods = ["burger", "fries", "salad", "soda", "ice cream"]

print("The restaurant offers:")
for food in foods:
    print(food)

print("\nNow attempting to change the first item in the list...")

# Tryd and error with turkey and it turned red
try:
    foods[0] = "turkey"
except TypeError as e:
    print(f"Error: {e}")

# The new menu items that are being added
print("The restaurant now offers:")
foods = ["turkey", "fries", "burger", "soda", "soup"]

# Reprints everything again but with an updated list
print("The updated foods offered are:")
for food in foods:
    print(food)
