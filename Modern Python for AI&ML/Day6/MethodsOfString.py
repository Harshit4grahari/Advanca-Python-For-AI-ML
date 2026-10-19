# Methods for String Manipulation

# 1. strip() - Removes leading and trailing whitespace from a string
string_with_whitespace = "   Hello, Python!   "
stripped_string = string_with_whitespace.strip()
print("Stripped String:", stripped_string)

# 2. replace(old, new) - Replaces occurrences of a substring with another substring
original_string = "I love Python programming."
new_string = original_string.replace("Python", "Java")
print("Original String:", original_string)
print("New String:", new_string)

# 3. split(delimiter) - Splits a string into a list of substrings based on a specified delimiter
fruits = "apple,banana,cherry,grape"
fruit_list = fruits.split(",")
print("Fruit List:", fruit_list)

# 4. join(iterable) - Joins elements of an iterable (like a list) into a single string with a specified delimiter
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print("Joined Sentence:", sentence)

# 5. upper() - Converts all characters in a string to uppercase
lowercase_string = "hello, world!"
uppercase_string = lowercase_string.upper()
print("Uppercase String:", uppercase_string)

# 6. lower() - Converts all characters in a string to lowercase
uppercase_string = "HELLO, WORLD!"
lowercase_string = uppercase_string.lower()
print("Lowercase String:", lowercase_string)

# 7. title() and capitalize() - Converts the first character of each word to uppercase (title case) or the first character of the string to uppercase (capitalize)
title_case_string = "python programming is fun"
capitalized_string = title_case_string.capitalize()
print("Title Case String:", title_case_string.title())
print("Capitalized String:", capitalized_string)

# 8. find(substring) - Returns the index of the first occurrence of a substring in a string, or -1 if not found
text = "I love programming in Python."
index = text.find("Python")
if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found.")

# 9. count(substring) - Returns the number of occurrences of a substring in a string
text = "Python is great. Python is versatile."
count = text.count("Python")
print("Number of occurrences of 'Python':", count)

# 10. isdigit() and isalpha() - Checks if all characters in a string are digits or alphabetic
numeric_string = "12345"
alphabetic_string = "HelloWorld"
print("Is numeric_string all digits?", numeric_string.isdigit())
print("Is alphabetic_string all alphabetic?", alphabetic_string.isalpha())

# 11. startswith(prefix) and endswith(suffix) - Checks if a string starts or ends with a specified prefix or suffix
filename = "example.txt"
print("Does filename start with 'example'?", filename.startswith("example"))
print("Does filename end with '.txt'?", filename.endswith(".txt"))

# 12. String Manipulation ASCII values: ord() and chr() - Converts a character to its ASCII value and vice versa
char = 'A'
ascii_value = ord(char)
print(f"ASCII value of '{char}':", ascii_value)
print(chr(65), "is the character for ASCII value 65.")