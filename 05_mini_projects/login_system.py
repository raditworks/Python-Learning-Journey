print("================================")
print("        LOGIN SYSTEM")
print("================================\n")

# predefined username and password
USERNAME = "DitMaster"
PASSWORD = "pythonBasics123"

chance = 0
# function to handle user login
def login():
    global chance
    if chance >= 3:
        print("Too many failed attempts! Please try again later.")
        return
    else:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == USERNAME and password == PASSWORD:
            print("Login successful! Welcome, ",USERNAME, "!")
            return False
        else:
            chance += 1
            print("Login failed! Invalid username or password.")

while True:
    if login() == False:
        break