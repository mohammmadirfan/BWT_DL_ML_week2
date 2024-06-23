# Week 2 Assignment
# BWT ML/DL Track 1

# Question 1: User Information Collection and Validation
def get_user_info():
    user_info = {}
    user_info['name'] = input("What's your name? ")
    user_info['age'] = input("How old are you? ")
    user_info['email'] = input("Enter your email address: ")
    
    # Check if the email is valid (contains "@" and ".")
    while "@" not in user_info['email'] or "." not in user_info['email']:
        print("Hmm, that doesn't look like a valid email. Try again.")
        user_info['email'] = input("Please enter a valid email address: ")

    user_info['favorite_number'] = input("What's your favorite number? ")

    # Print out a nice message with their info
    print(f"Hi {user_info['name']}! You're {user_info['age']} years old, your email is {user_info['email']}, and your favorite number is {user_info['favorite_number']}.")

# Question 2: Check if a Number is Even or Odd
def is_even(number):
    # Simple check using the modulus operator
    if number % 2 == 0:
        return True
    else:
        return False

# Question 3: Temperature Conversion
def convert_temperature(temp, scale):
    # Convert temperature from one scale to the other
    if scale.upper() == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif scale.upper() == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        # Handle invalid scale input
        print("Oops! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return None
    return converted_temp

# Question 4: Find Maximum and Minimum in a List
def find_max_min(numbers_list):
    # Using Python's built-in functions to find max and min
    max_number = max(numbers_list)
    min_number = min(numbers_list)
    return max_number, min_number

# Question 5: Collect and Store Student Data
def collect_student_data():
    students = []

    # Get details for 3 students
    for _ in range(3):
        name = input("What's the student's name? ")
        age = input("How old are they? ")
        grade = input("What's their grade? ")
        students.append((name, age, grade))

    # Convert list of tuples into a dictionary
    students_dict = {student[0]: (student[1], student[2]) for student in students}

    # Print out the student details
    for name, details in students_dict.items():
        print(f"Student Name: {name}, Age: {details[0]}, Grade: {details[1]}")

# Question 6: Update Inventory
def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        # Update item quantity, ensure it doesn't drop below zero
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    else:
        print(f"Item '{item}' isn't in the inventory.")
    return inventory_dict

if __name__ == "__main__":
    # Execute Question 1
    print("Question 1:")
    get_user_info()
    print("\n")

    # Execute Question 2
    print("Question 2:")
    number = int(input("Enter a number: "))
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    print("\n")

    # Execute Question 3
    print("Question 3:")
    temp = float(input("Enter the temperature: "))
    scale = input("Is it in Celsius (C) or Fahrenheit (F)? ")
    convert_temperature(temp, scale)
    print("\n")

    # Execute Question 4
    print("Question 4:")
    numbers_list = []
    for _ in range(5):
        number = float(input("Enter a number: "))
        numbers_list.append(number)

    max_num, min_num = find_max_min(numbers_list)
    print(f"The largest number is: {max_num}")
    print(f"The smallest number is: {min_num}")
    print("\n")

    # Execute Question 5
    print("Question 5:")
    collect_student_data()
    print("\n")

    # Execute Question 6
    print("Question 6:")
    # Starting inventory
    inventory = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grapes": 15,
        "mango": 7
    }

    for _ in range(3):
        item = input("Enter the item name to update: ")
        quantity = int(input(f"Enter the quantity to add/remove for {item} (negative to remove): "))
        inventory = update_inventory(inventory, item, quantity)

    # Show the updated inventory
    print("Updated Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
