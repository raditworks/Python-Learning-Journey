print("===============================")
print(" FUNCTION PARAMETERS IN PYTHON")
print("===============================\n")

# defining a function with multiple parameters
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# calling the function with arguments
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
greet_user(user_name, user_age)