# Alex Torbica
# Chapter 4

# Prints the cubes of numbers from 1 to 10 using a set comprehension and then prints each cube on a new line
cubes = {number ** 3 for number in range(1, 11)}

# Sets a loop to print the number in the set of cubes
for cube in cubes:
    print(cube)