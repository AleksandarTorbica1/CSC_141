# Alex Torbica
# Chapter 6 
# Same as previously also another dictiornary that has key value pairs and then prints out in a for loop. To create a glossary of terms and definitions in each sentence.

Glossary = {
    'dictionary': "A collection of key-value pairs.",
    'key': "A unique identifier used to access a value in a dictionary.",
    'value': "The data associated with a key in a dictionary.",
    'item': "A key-value pair in a dictionary.",
    'get': "A method used to retrieve a value from a dictionary using its key.",
}

for word, meaning in Glossary.items():
    print(f"{word.title()}:\n {meaning}\n")