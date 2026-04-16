print("================================")
print("    DICTIONARIES IN PYTHON")
print("================================\n")

# creating a dictionary
person = {
    "name" : "Raditya Syafi W",
    "age" : 19,
    "address" : "JL. Gatot Subroto"
}

# printing the dictionary
print("Person Dictionary:", person)

# access value using key
print("Name:", person["name"])
print("Age:", person["age"])
print("Address:", person["address"])

# adding a new key-value pair
person["email"] = "test123@gmail.com"
print("Person Dictionary after adding email:", person)

# updating a value
person["age"] = 20
print("Person Dictionary after updating age:", person)
