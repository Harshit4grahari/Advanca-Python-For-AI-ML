# Convert Tuple to List:

colors = ("red", "orange", "white", "yellow")
colors_list = list(colors)

print(colors_list)

# Now we can Modify the Tuple As List

colors_list.append("blue")
print(colors_list)

# then Convert List Into Tuple

colors_tuples = tuple(colors_list)
print(colors_tuples)