# Strings in Python
# Strings are sequences of characters enclosed in single quotes, double quotes, or triple quotes. They
# can be manipulated using various string methods and operations.

# Example 1: Creating strings

# Using single quotes
string1 = 'Hello, World!'

# Using double quotes
string2 = "Python is awesome!"

# Using triple quotes for multi-line strings
string3 = '''This is a multi-line string.
It can span multiple lines.'''

print(string1)
print(string2)
print(string3)

# Example 2: String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenating strings using the + operator
print("Full Name:", full_name)

# Example 3: String indexing and slicing [start:end:step] - Accessing individual characters or substrings
sample_string = "Python Programming"
print("First character:", sample_string[0])
print("Last character:", sample_string[-1])
print("Substring from index 0 to 6:", sample_string[0:7])
print("Substring from index 7 to 13:", sample_string[7:14])
print("Every second character:", sample_string[::2])
print("Every third character:", sample_string[::3])

# Example 4: String Formatting using f-strings (available in Python 3.6 and later)
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

# Example 5: String Formatting using format() method
greeting = "Hello, {}. Welcome to {}!"
formatted_greeting = greeting.format("Bob", "Python Programming")
print(formatted_greeting)
