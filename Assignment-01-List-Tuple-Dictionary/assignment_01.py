# Assignment 1
# Different Operations on List, Tuple and Dictionary

# ---------------- LIST ----------------

my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)

# append()
my_list.append(60)
print("After append():", my_list)

# insert()
my_list.insert(2, 25)
print("After insert():", my_list)

# remove()
my_list.remove(30)
print("After remove():", my_list)

# pop()
my_list.pop()
print("After pop():", my_list)

# sort()
my_list.sort()
print("After sort():", my_list)


# ---------------- TUPLE ----------------

my_tuple = (10, 20, 30, 20, 40)

print("\nOriginal Tuple:", my_tuple)

# count()
print("Count of 20:", my_tuple.count(20))

# index()
print("Index of 30:", my_tuple.index(30))

# len()
print("Length of Tuple:", len(my_tuple))

# slicing
print("Tuple Slicing:", my_tuple[1:4])


# ---------------- DICTIONARY ----------------

my_dict = {
    "Name": "Aayushi",
    "Age": 18,
    "Course": "Computer Science"
}

print("\nOriginal Dictionary:", my_dict)

# keys()
print("Keys:", my_dict.keys())

# values()
print("Values:", my_dict.values())

# items()
print("Items:", my_dict.items())

# update()
my_dict.update({"Age": 19})
print("After update():", my_dict)

# pop()
my_dict.pop("Age")
print("After pop():", my_dict))
