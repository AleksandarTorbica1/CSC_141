# Alex Torbica
# Chapter 6
# Same functions and for loop print but with more terms and definitions added to the dictionary

Glossary = {
    'dictionary': "A collection of key-value pairs.",
    'key': "A unique identifier used to access a value in a dictionary.",
    'keys': "A method used to retrieve all the keys in a dictionary.",
    'integer': "A whole number with no decimal point.",
    'value': "The data associated with a key in a dictionary.",
    'item': "A key-value pair in a dictionary.",
    'get': "A method used to retrieve a value from a dictionary using its key.",
    'comment': "A note in the code that is ignored by the interpreter and is used to explain the code to humans.",
    'string': "A sequence of characters enclosed in quotes.",
    'loop': "A programming construct that repeats a block of code multiple times.",
}

for word, meaning in Glossary.items():
    print(f"{word.title()}:\n {meaning}\n")