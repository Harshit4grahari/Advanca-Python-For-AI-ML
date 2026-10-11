# Operators in Python
# Operators are special symbols that perform operations on variables and values. Python has several types of operators


#1. Arithmetic Operators: Used to perform mathematical operations like addition, subtraction, multiplication, etc.
a = 10
b = 3
print("Addition:", a + b) # Addition
print("Subtraction:", a - b) # Subtraction
print("Multiplication:", a * b) # Multiplication
print("Division:", a / b) # Division
print("Modulus:", a % b) # Modulus
print("Exponentiation:", a ** b) # Exponentiation

#2. Comparison Operators: Used to compare two values and return a boolean result (True or False).
x = 5
y = 10
print("Equal:", x == y) # Equal
print("Not Equal:", x != y) # Not Equal
print("Greater than:", x > y) # Greater than
print("Less than:", x < y) # Less than
print("Greater than or equal to:", x >= y) # Greater than or equal to
print("Less than or equal to:", x <= y) # Less than or equal to

#3. Logical Operators: Used to combine conditional statements.
p = True
q = False
print("Logical AND:", p and q) # Logical AND
print("Logical OR:", p or q) # Logical OR
print("Logical NOT:", not p) # Logical NOT

#4. Assignment Operators: Used to assign values to variables.
m = 5
m += 3 # Equivalent to m = m + 3
print("Assignment Operator (+=):", m) # Assignment Operator (+=)
m -= 2 # Equivalent to m = m - 2
print("Assignment Operator (-=):", m) # Assignment Operator (-=)
m *= 2 # Equivalent to m = m * 2
print("Assignment Operator (*=):", m) # Assignment Operator (*=)
m /= 2 # Equivalent to m = m / 2
print("Assignment Operator (/=):", m) # Assignment Operator (/=)
m %= 2 # Equivalent to m = m % 2
print("Assignment Operator (%=):", m) # Assignment Operator (%=)
m **= 2 # Equivalent to m = m ** 2
print("Assignment Operator (**=):", m) # Assignment Operator (**=)

#5. Bitwise Operators: Used to perform bit-level operations on binary numbers.
x = 5 # Binary: 0101
y = 3 # Binary: 0011
print("Bitwise AND:", x & y) # Bitwise AND
print("Bitwise OR:", x | y) # Bitwise OR
print("Bitwise XOR:", x ^ y) # Bitwise XOR
print("Bitwise NOT:", ~x) # Bitwise NOT
print("Left Shift:", x << 1) # Left Shift
print("Right Shift:", x >> 1) # Right Shift

#6. Membership Operators: Used to test if a value is present in a sequence (like a list, tuple, or string).
fruits = ["apple", "banana", "cherry"]
print("Membership Operator (in):", "banana" in fruits) # Membership Operator (in)
print("Membership Operator (not in):", "grape" not in fruits) # Membership Operator (not in)
