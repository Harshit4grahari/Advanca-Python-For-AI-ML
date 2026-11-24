# Dictionary in Python
# A dictionary is a built-in datatype that lets us create a collection of key-value pairs.

# Example of Dictionary:

student = {
    "name": "Harshit",
    "age": 22,
    "grade": "A"
}
# Key  -> name, age, grade
# Value -> Harshit, 22, A

# Accessing Values in a Dictionary
print(student["name"])  # Output: Harshit
print(student.get("age"))   # Output: 22
print(type(student.get("grade"))) # Output: <class 'str'>


# Creating a Empty Dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Avoiding KeyError in Dictionary
# We can use the get() method to avoid KeyError when accessing a key that may not
# exist in the dictionary. The get() method returns None if the key is not found, instead of raising an error.


# Adding and Updating
student["email"] = "harshit@example.com"  # Adding a new key-value pair
student["age"] = 23  # Updating an existing value


# Removing items from a Dictionary
# We can remove items from a dictionary using the del statement or the pop() method.
del student["grade"]  # Removing a key-value pair
student.pop("email")  # Removing a key-value pair using pop()
# student.clear()  # Removing all items from the dictionary


# Dictionary Methods
print(student.keys())   # Output: dict_keys(['name', 'age'])
print(student.values()) # Output: dict_values(['Harshit', 23])
print(student.items())  # Output: dict_items([('name', 'Harshit'), ('age', 23)])


# Iterating Through a Dictionary
for key, value in student.items():
    print(f"{key}: {value}")