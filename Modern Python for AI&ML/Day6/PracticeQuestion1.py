# Reverse String / Palindrome

text = "Harshit"
print("Reverse of the string:", text[::-1])  # Using slicing to reverse the string

# Check if the string is a palindrome
if text == text[::-1]:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")

word = "level"
print("Reverse of the string:", word[::-1])
# Check if the string is a palindrome
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")