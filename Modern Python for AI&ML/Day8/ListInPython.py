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

# List Slicing: list_name[start:end:step]
print(groceries[0:2])
print(groceries[:3])
print(groceries[1:])
print(groceries[::-1])

# List Comprehension:
num = [11,22,33,44,55,66]
sqr = [x*x for x in num]
print(sqr)

sqrs = [x*x for x in range(11)]
print(sqrs)

# Nested List
matrix = [[1,2], [3,4], [4,5]]
print(matrix)
print(matrix[1][0])

# Sorting & Reversing
num.sort()
print(num)

num.reverse()
print(num)