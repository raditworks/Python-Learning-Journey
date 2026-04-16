print("================================")
print("         LISTS IN PYTHON")
print("================================\n")

# creating a list
fruits = ["apple", "banana", "orange", "grape"]
print(f"Original list: {fruits}")

# accessing elements in a list
print(f"First fruit: {fruits[0]}") # the first index is 0
print(f"Last fruit: {fruits[-1]}")

# modifying elements in a list
fruits[1] = "mango"
print(f"Modified list: {fruits}")

# adding elements to a list
fruits.append("pineapple")
print(f"List after adding an element: {fruits}")

# removing elements from a list
fruits.remove("orange")
print(f"List after removing an element: {fruits}")