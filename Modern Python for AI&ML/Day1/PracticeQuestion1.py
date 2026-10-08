# Swap two numbers 

#Method 1: Using a temporary variable
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")

#Method 2: Without using a temporary variable
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")