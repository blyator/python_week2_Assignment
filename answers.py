# Create an empty list

my_list = []

# Appending elements

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting 15 at the second position

my_list.insert(1, 15)

# Extending with [50, 60, 70]

my_list.extend([50, 60, 70])

# Removing the last element

my_list.pop()

#  Sorting in ascending order

my_list.sort()

# Find and print the index of value 30

index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
