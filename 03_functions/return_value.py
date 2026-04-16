print("===========================")
print("   RETURN VALUE IN PYTHON")
print("===========================\n")

# defining a function that returns a value
def calculate_area(length, width):
    area = length * width
    return area

# calling the function and storing the returned value
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")