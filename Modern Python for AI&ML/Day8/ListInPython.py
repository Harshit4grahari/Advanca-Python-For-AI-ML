# List in Python:
# A list is a collection of items that is ordered, changeable and allows duplicate.(Like a shopping list- can add, remove and replace items)

# Creating of List:
groceries = ["milk", 'noodles', "bread", "rice", "sauce"]
print(groceries)
print(type(groceries))

# Accessing Elements:
print(groceries[1])
print(groceries[-1])

# Modifying a List:
groceries[0] = "wheat"
print(groceries)

# Adding ELements
groceries.append("grapes") #add elements in last
print(groceries)

groceries.insert(1, "apples")
print(groceries)

# Removing Elements
groceries.remove("apples")
print(groceries)

groceries.pop #remove last element
print(groceries)

del groceries[0]
print(groceries)

# Length and Looping
print(len(groceries)) #print the length of list

for items in groceries: #looping in list to access every elements sequentially
    print(items)
