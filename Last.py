import os
import random
import time
from typing import List, Union

# --- Configuration ---
PROJECT_AUTHOR = "Kirt"
ACTIVITY_COUNT = 25
CHALLENGE_COUNT = 15

# --- Utility Functions ---

def clear_screen():
    """Clears the console screen."""
    # Use 'cls' for Windows, 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Prompts the user to press Enter to continue."""
    input("\nPress Enter to return to the menu...")

# --- Activity Functions (Core Concepts) ---

def activity_1_hello_world():
    """Prints a classic 'Hello, World!' message."""
    print("--- Activity 1: Hello World ---")
    print('Hello World')

def activity_2_user_greeting():
    """Takes user input for a name and prints a personalized greeting."""
    print("--- Activity 2: Personalized Greeting ---")
    name = input("Enter your Name: ")
    print(f"Hi {name}! Welcome to the project menu.")

def activity_3_escape_sequences():
    """Demonstrates various Python escape sequences (\n, \t, \\, \r, \f)."""
    print("--- Activity 3: Escape Sequences Demo ---")
    print("1. Newline and Tab:")
    print("Good Morning!\n\tBSIT-1C Python Class") # \n and \t
    print("2. Double Backslash (for file paths):")
    print("File path: C:\\Users\\Student\\Files") # \\
    print("3. Carriage Return (often overwrites on the same line):")
    print("\rStarting... \rFinished!") # \r
    print("4. Form Feed (often acts like a newline/space depending on terminal):")
    print("Line One\fLine Two") # \f

def activity_4_string_methods_len():
    """Takes a name, capitalizes it, and counts its length."""
    print("--- Activity 4: String Methods and Length ---")
    name = input("Enter a name: ")
    capitalized_name = name.capitalize()
    print(f"Welcome to the system, {capitalized_name}")
    print(f"Your name has {len(capitalized_name)} characters.")

def activity_5_data_type_check():
    """Uses eval() to determine the data type of user input."""
    print("--- Activity 5: Data Type Check (using eval) ---")
    try:
        # NOTE: eval() is powerful but generally unsafe for external input.
        # It's used here for educational demo of type conversion.
        user_input = input("Type a value (e.g., 5, 5.0, 'hello', [1,2]): ")
        x = eval(user_input)
        print(f"The input value is: {x}")
        print(f"The data type is: {type(x)}")
    except Exception as e:
        print(f"Error evaluating input: {e}")
        print("Could not determine a valid Python type.")

def activity_6_arithmetic_operators():
    """Performs and displays results for all basic arithmetic operators."""
    print("--- Activity 6: Arithmetic Operators ---")
    try:
        no1 = float(input("Enter the first number (no1): "))
        no2 = float(input("Enter the second number (no2): "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    ans1 = no1 + no2
    ans2 = no1 - no2
    ans3 = no1 * no2
    ans6 = no1 ** no2

    if no2 != 0:
        ans4 = no1 / no2
        ans5 = no1 % no2
        ans7 = no1 // no2
    else:
        ans4 = "Undefined (Div/0)"
        ans5 = "Undefined (Mod/0)"
        ans7 = "Undefined (FloorDiv/0)"

    print(f"\nResults for {no1} and {no2}:")
    print(f"Sum (no1 + no2): {ans1}")
    print(f"Difference (no1 - no2): {ans2}")
    print(f"Product (no1 * no2): {ans3}")
    print(f"Quotient (no1 / no2): {ans4}")
    print(f"Remainder (no1 % no2): {ans5}")
    print(f"Exponent (no1 ** no2): {ans6}")
    print(f"Floor Division (no1 // no2): {ans7}")

def activity_7_assignment_operators():
    """Demonstrates compound assignment operators (+=, *=)."""
    print("--- Activity 7: Assignment Operators ---")
    amount = 5
    print(f"Initial amount: {amount}")

    amount += 5  # amount = amount + 5
    print(f"After amount += 5: {amount}")

    amount += 60
    amount *= 2  # amount = amount * 2
    print(f"After amount += 60 then amount *= 2: {amount}")

def activity_8_comparison_operators():
    """Demonstrates comparison operators (<, !=) resulting in boolean values."""
    print("--- Activity 8: Comparison Operators ---")
    a = 3
    b = 5

    print(f"Is a ({a}) less than b ({b})? Result: {a < b}")

    name1 = "Jasmine"
    name2 = "Jasmine"
    name3 = "kirt"

    print(f"Is name1 ('{name1}') not equal to name2 ('{name2}')? Result: {name1 != name2}")
    print(f"Is name1 ('{name1}') not equal to name3 ('{name3}')? Result: {name1 != name3}")

def activity_9_logical_operators():
    """Demonstrates the 'and' logical operator."""
    print("--- Activity 9: Logical Operators (and) ---")
    username_correct = 'cutepotato'
    password_correct = 'friesandicecream'

    print("Checking predefined login credentials with 'and':")
    # Case 1: Correct credentials (True and True -> True)
    print(f"Result for ('{username_correct}' == 'cutepotato') and ('{password_correct}' == 'friesandicecream'):")
    print( (username_correct == 'cutepotato') and ( password_correct == 'friesandicecream' ) )

    # Case 2: Incorrect username (False and True -> False)
    print(f"Result for ('incorrect' == 'cutepotato') and ('{password_correct}' == 'friesandicecream'):")
    print( ('incorrect' == 'cutepotato') and ( password_correct == 'friesandicecream' ) )

def activity_10_simple_if_else():
    """Implements a simple login check using if/else and logical 'and'."""
    print("--- Activity 10: Simple If-Else Login ---")
    username_correct = 'cutepotato'
    password_correct = 'friesandicecream'

    u = input("USERNAME --> ")
    p = input("PASSWORD --> ")

    if (u == username_correct) and (p == password_correct):
        print("✅ Access granted")
    else:
        print("❌ Access Denied")

def activity_11_elif_ladder():
    """Uses an extensive elif ladder to categorize temperature input."""
    print("--- Activity 11: Elif Ladder Temperature Check ---")
    try:
        temp = float(input("Enter temperature (°C) --> "))
    except ValueError:
        print("Invalid input. Please enter a numerical temperature.")
        return

    if 1 <= temp <= 20:
        print("The temperature is considered extremely cold.")
    elif 21 <= temp <= 30:
        print("The temperature is moderately cold.")
    elif 31 <= temp <= 37:
        print("The temperature is normal.")
    elif 38 <= temp <= 45:
        print("The temperature is hot.")
    elif 46 <= temp <= 50:
        print("The temperature is boiling hot.")
    elif temp > 50:
        print("The temperature is dangerous!")
    else:
        print("The temperature is invalid (or below 1°C).")

def activity_12_basic_for_loop():
    """A basic for loop that runs 10 times."""
    print("--- Activity 12: Basic For Loop (1-10) ---")
    print("Running a loop 10 times:")
    for cycle in range(1, 11):
        print(f"Loop {cycle}: BSIT 1C - Magandang Hapon")

def activity_13_for_loop_accumulator():
    """Uses a for loop to accumulate the sum of 10 user-entered numbers."""
    print("--- Activity 13: For Loop Accumulator ---")
    total_sum = 0
    num_inputs = 5 # Reduced to 5 for quicker demo

    print(f"Enter {num_inputs} numbers. We will calculate the total sum.")
    for i in range(1, num_inputs + 1):
        try:
            number = float(input(f"[{i}/{num_inputs}] Enter a number: "))
            total_sum += number
        except ValueError:
            print("Invalid input. Skipping this entry.")
            continue

    print(f"\n\tThe sum of all valid numbers is: {total_sum:.2f}")

def activity_14_for_loop_countdown():
    """A for loop that counts down from 20 to 1."""
    print("--- Activity 14: For Loop Countdown (20 to 1) ---")
    print("Starting countdown:")
    for i in range(20, 0, -1):
        print(i, end=" ")
    print("\nCountdown complete.")

def activity_15_nested_loops_simple_box():
    """Demonstrates nested loops to create a simple 10x10 pattern (box of numbers)."""
    print("--- Activity 15: Nested Loops (Box Pattern) ---")
    for i in range(1, 6): # Reduced to 5x5 for clarity
        for x in range(1, 6):
            print(x, end=" ")
        print(f"(Row {i})") # Prints the outer loop variable

def activity_16_nested_loops_right_triangle():
    """Creates a right-angled triangle pattern using numbers."""
    print("--- Activity 16: Nested Loops (Right Triangle - Numbers) ---")
    for i in range(1, 6): # Outer loop controls rows (1 to 5)
        for x in range(1, i + 1): # Inner loop controls columns (prints up to current row number)
            print(x, end=" ")
        print() # Newline after each row

def activity_17_nested_loops_inverted_right_triangle():
    """Creates an inverted right-angled triangle pattern using asterisks."""
    print("--- Activity 17: Nested Loops (Inverted Right Triangle - Asterisks) ---")
    #     for i in range(5, 0, -1): # Outer loop counts down (5 to 1)
        for x in range(i): # Inner loop prints i asterisks
            print("*", end=" ")
        print()

def activity_18_nested_loops_pyramid_right_side():
    """Creates a right-aligned triangle pattern using spaces and asterisks."""
    print("--- Activity 18: Nested Loops (Right-Aligned Triangle - Asterisks) ---")
    #     num_rows = 5
    for i in range(1, num_rows + 1):
        # 1. Print leading spaces
        print("  " * (num_rows - i), end="")
        # 2. Print asterisks
        print("* " * i)

# --- WIP Activities Implemented ---

def activity_19_while_loop_input_check():
    """(WIP Implemented) Uses a while loop to ensure valid input is provided."""
    print("--- Activity 19: Input Validation with While Loop ---")
    is_valid = False
    age = 0
    while not is_valid:
        try:
            age = int(input("Enter your age (must be > 18): "))
            if age > 18:
                is_valid = True
            else:
                print("You must be older than 18 to proceed.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"Validation successful. Your age is {age}.")

def activity_20_simple_list_manipulation():
    """(WIP Implemented) Demonstrates basic list operations (append, remove, print)."""
    print("--- Activity 20: List Manipulation (Add/Remove) ---")
    groceries = ["Milk", "Bread", "Eggs"]
    print(f"Initial List: {groceries}")

    new_item = input("What item would you like to add? ")
    groceries.append(new_item)
    print(f"List after adding '{new_item}': {groceries}")

    try:
        remove_item = input("What item would you like to remove? ")
        groceries.remove(remove_item)
        print(f"List after removing '{remove_item}': {groceries}")
    except ValueError:
        print(f"Item '{remove_item}' not found in the list.")

# --- While Loop & List Activities ---

def activity_21_number_guessing_game():
    """A number guessing game using a while loop."""
    print("--- Activity 21: Number Guessing Game ---")
    print("Guess the number between 1 and 5.")

    random_value = random.randint(1, 5)
    tries = 0
    
    while True:
        try:
            num = int(input("Guess the number --> "))
            if not 1 <= num <= 5:
                 print("Please enter a number only between 1 and 5.")
                 continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        tries += 1
        if num == random_value:
            print("\n🎉 WINNER!!!")
            print(f"Hi, your guess is correct. It took you {tries} tries.")
            break
        else:
            print("Mali ang hula mo boi. Try again.")

def activity_22_while_loop_exit_control():
    """A while loop controlled by user input for a simple simulated task."""
    print("--- Activity 22: While Loop (User-Controlled Exit) ---")
    is_dirty = True
    while is_dirty:
        washing = input("Continue washing cloths? (yes/no): ").lower().strip()

        if washing == "yes":
            print("Washing cloths now.... (Still dirty!)")
            # In a real app, logic here would determine if is_dirty becomes False
            continue
        elif washing == "no":
            print("Stopped washing cloths...")
            is_dirty = False # Explicitly set to False to end the loop
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
    print("Washing cycle finished.")

def activity_23_list_iteration_and_reverse():
    """Demonstrates iterating over a list and reversing it."""
    print("--- Activity 23: List Iteration and Reverse ---")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
    
    print("Original List Iteration:")
    for month in months:
        print(f"- Month of {month}")
    
    # Create a *copy* and reverse the copy to show the change clearly
    reversed_months = months[:] # Slicing creates a copy
    reversed_months.reverse()
    
    print("\nOriginal List (unchanged):", months)
    print("Reversed List:", reversed_months)

def activity_24_simple_dictionary_usage():
    """(WIP Implemented) Demonstrates a dictionary and accessing its values."""
    print("--- Activity 24: Simple Dictionary Usage ---")
    student = {
        "name": "Jasmine",
        "course": "BSIT-1C",
        "age": 19,
        "active": True
    }

    print("Student Information:")
    print(f"Name: {student['name']}")
    print(f"Course: {student['course']}")
    student['age'] += 1 # Update a value
    print(f"Updated Age: {student['age']}")

def activity_25_function_with_return():
    """(WIP Implemented) Demonstrates a simple function that takes arguments and returns a value."""
    print("--- Activity 25: Function with Return Value ---")
    
    def calculate_area(length: float, width: float) -> float:
        """Calculates the area of a rectangle."""
        return length * width

    try:
        L = float(input("Enter length: "))
        W = float(input("Enter width: "))
        area = calculate_area(L, W)
        print(f"A rectangle with length {L} and width {W} has an area of {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


# --- Code Challenge Functions (Application) ---

def challenge_1_ascii_art():
    """Prints complex ASCII art."""
    print("--- Code Challenge 1: ASCII Art Design ---")
    print("\t\t\t  *\n\t\t      *\t      *\n\t\t  *\t\t  *\n\t      * \tHi\t      *\n\t  *\t\tKirt\t          *\n\t      *\t\t\t"
        "      *\n\t\t  *\t\t  *\n\t\t       *\t      *\n\t\t\t  *")

def challenge_2_currency_breakdown():
    """Calculates the breakdown of a deposit amount into various bills (1000s, 500s, etc.)."""
    print("--- Code Challenge 2: Currency Breakdown ---")
    try:
        amount = int(input("Enter amount to deposit (integer only): "))
        if amount < 0:
            print("Amount must be non-negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print ("\nHere is a breakdown of your deposit:")
    
    # Define bill denominations from largest to smallest
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    results = {}
    current_amount = amount

    for bill in denominations:
        count = current_amount // bill
        current_amount %= bill
        results[bill] = count

    for bill, count in results.items():
        print(f"{count:<4} - ₱{bill}s")
    
    if current_amount > 0:
        print(f"Note: ₱{current_amount} was unallocated due to remaining fractional amount.")

def challenge_3_student_fare_discount():
    """Calculates and applies a student discount to a fare."""
    print("--- Code Challenge 3: Student Fare Discount ---")
    name = input("Enter your name: ")

    try:
        fare = float(input("How much is your fare: ₱"))
        if fare <= 0:
            print("Fare must be a positive amount.")
            return
    except ValueError:
        print("Invalid fare amount.")
        return
        
    student_status = input("Are you a Student (Yes/No)? ").lower().strip()
    
    disc = 0.20 # 20% discount
    
    print(f"\nHello, {name}")
    print(f"The original fare is: ₱{fare:.2f}")

    if student_status == 'yes':
        disc_amount = fare * disc
        disc_fare = fare - disc_amount
        print(f"The student discount amount (20%) is: ₱{disc_amount:.2f}")
        print(f"The discounted fare is: ₱{disc_fare:.2f}")
    else:
        print("You are not eligible for a student discount.")
        print(f"The regular fare remains: ₱{fare:.2f}")

    print("\nThank you for using the program.")

def challenge_4_manga_recommendator():
    """A conditional logic tree (if/elif/else) to recommend a manga based on criteria."""
    print("--- Code Challenge 4: Manga Recommendator ---")
    print("Welcome to the manga recommendator!")
    
    genre = input("What genre of manga would you like? (Action/Romance/Horror): ").strip().capitalize()
    
    if genre in ["Action", "Romance", "Horror"]:
        length = input("Nice! What do you prefer? (Short/Medium/Long): ").strip().capitalize()
        
        if length in ["Short", "Medium", "Long"]:
            decade = input("What decade do you want? (2000/2010): ").strip()
            
            recommendation = "No specific recommendation found. Try something popular." # Default

            if genre == "Action":
                if length == "Long" and decade == "2000":
                    recommendation = "One Piece"
                elif length == "Medium" and decade == "2010":
                    recommendation = "Attack on Titan"
                elif length == "Short" and decade == "2010":
                    recommendation = "Zero Two"
                else:
                    recommendation = "Clover (Considered a hidden gem)"

            elif genre == "Romance":
                if length == "Short" and decade == "2000":
                    recommendation = "Ballroom e Youkoso"
                elif length == "Medium" and decade == "2010":
                    recommendation = "Ao Haru Ride"
                elif length == "Long" and decade == "2010":
                    recommendation = "Kimi ni Todoke"
                else:
                    recommendation = "Horimiya (Modern classic)"

            elif genre == "Horror":
                if length == "Short" and decade == "2000":
                    recommendation = "Mononoke"
                elif length == "Medium" and decade == "2010":
                    recommendation = "Tokyo Ghoul"
                elif length == "Long" and decade == "2000":
                    recommendation = "Hellsing"
                else:
                    recommendation = "Parasyte (Focus on psychological horror)"

            print(f"\nBased on your choices, I recommend: **{recommendation}**")
        else:
            print("Invalid length input. Please type Short, Medium, or Long.")
    else:
        print("Invalid Genre. Please choose from Action, Romance, or Horror.")

def challenge_5_factorial_calculator():
    """Calculates the factorial of a user-input number using a for loop."""
    print("--- Code Challenge 5: Factorial Calculator ---")
    try:
        a = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if a < 0:
        print("Factorial is not defined for negative numbers.")
    elif a == 0:
        print("The factorial of 0 is 1.")
    else:
        # 5! = 5 * 4 * 3 * 2 * 1
        factor = 1
        # Loop from the number down to 1
        for i in range(a, 0, -1):
            factor *= i 

        print(f"The factorial of {a} is {factor}")

def challenge_6_fibonacci_sequence_generator():
    """(WIP Implemented) Generates the Fibonacci sequence up to a given term."""
    print("--- Code Challenge 6: Fibonacci Sequence Generator ---")
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence (e.g., 10): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    a, b = 0, 1
    count = 0
    fib_list = []
    
    if n == 1:
        fib_list.append(a)
    elif n > 1:
        while count < n:
            fib_list.append(a)
            # Calculate the next term
            nth = a + b
            # Update values
            a = b
            b = nth
            count += 1
            
    print(f"\nThe Fibonacci sequence (first {n} terms):\n{fib_list}")


def challenge_7_odd_numbers_accumulator():
    """Accumulates the sum of only the odd numbers from 10 user inputs."""
    print("--- Code Challenge 7: Odd Numbers Accumulator ---")
    print("Enter 10 numbers. We'll help you sum only the odd ones!")

    odd_sum = 0
    
    for i in range(1, 11):
        try:
            num = int(input(f"[{i}/10] Enter number: "))
            # Check for oddness (remainder is not 0 when divided by 2)
            if num % 2 != 0:
                odd_sum += num
        except ValueError:
            print("Invalid input, skipping this entry.")
            continue

    print(f"\nSum of all odd numbers entered: {odd_sum}")

def challenge_8_multiplication_table():
    """Generates the multiplication table for a user-specified number."""
    print("--- Code Challenge 8: Multiplication Table Creator ---")
    try:
        num = int(input("Enter a number to create its multiplication table (up to x10): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print(f"\nMultiplication table for {num}:")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def challenge_9_spaceship_countdown():
    """Implements a countdown timer using a for loop."""
    print("--- Code Challenge 9: Spaceship Countdown Timer ---")

    try:
        start_num = int(input("Enter the starting number for countdown (e.g., 10): "))
        if start_num <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print("\nCountdown started:")

    for i in range(start_num, 0, -1):
        print(i)
        time.sleep(0.3) # Added a small delay for dramatic effect

    print("🚀 Liftoff!")

def challenge_10_inverted_triangle_pattern():
    """Creates a full inverted triangle pattern using nested loops."""
    print("--- Code Challenge 10: Inverted Triangle Pattern ---")
    num_rows = 10
    for i in range(num_rows, 0, -1):
        # 1. Print leading spaces (for alignment)
        print(" " * (num_rows - i), end="")
        # 2. Print asterisks
        print("*" * (2 * i - 1))

def challenge_11_diamond_pattern():
    """Creates a diamond shape using two sets of nested loops."""
    print("--- Code Challenge 11: Diamond Pattern ---")
    num_rows = 5 # Half the diamond height

    # Top half of the diamond (including the widest row)
    for i in range(1, num_rows + 1):
        print(" " * (num_rows - i), end="")
        print("*" * (2 * i - 1))

    # Bottom half of the diamond (excluding the widest row)
    for i in range(num_rows - 1, 0, -1):
        print(" " * (num_rows - i), end="")
        print("*" * (2 * i - 1))

def challenge_12_number_pyramid_pattern():
    """Creates a symmetrical number pyramid pattern using nested loops."""
    print("--- Code Challenge 12: Symmetrical Number Pyramid ---")
    num_rows = 6 
    for i in range(1, num_rows + 1):
        # 1. Print leading spaces for center alignment
        print(" " * (num_rows - i), end="")
        
        # 2. Print numbers descending (e.g., 3 2 1)
        for y in range(i, 0, -1):
            print(y, end="")
            
        # 3. Print numbers ascending (e.g., 2 3 4)
        for z in range(2, i + 1):
            print(z, end="")
        
        print()

def challenge_13_odd_number_collector():
    """Collects and sums odd numbers using a while loop, terminating on '0'."""
    print("--- Code Challenge 13: Odd Number Collector ---")
    name = input("Enter your name: ")
    print("Enter odd numbers (type 0 to stop and get the sum).")

    odd_sum = 0
    odd_numbers_list = []
    
    while True:
        try:
            number = float(input("Enter an odd number (or 0): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        # Check for termination condition
        if number == 0:
            print("Loop terminated.")
            break
            
        # Check for odd number (must be an integer and odd)
        # Check if it's a whole number first
        if number == int(number) and number % 2 != 0: 
            print("✅ ODD NUMBER DETECTED")
            odd_sum += int(number)
            odd_numbers_list.append(int(number))
        elif number == int(number) and number % 2 == 0:
            print("❌ EVEN NUMBER DETECTED. Only odd numbers are summed.")
        else:
            print("Input is not a whole number.")


    print(f"\nHi {name}, the sum of all odd numbers is {odd_sum}")
    print(f"ODD NUMBERS entered: {odd_numbers_list}")

def challenge_14_list_input_collector():
    """Collects user input into a list until a specific exit command is given."""
    print("--- Code Challenge 14: Anime List Collector ---")
    anime_list: List[str] = [] # Use type hinting for clarity
    
    while True:
        a_list = input("Enter an anime (or type 'exit' to stop): ").strip()
        
        if a_list.lower() == "exit":
            print("You have exited the anime entry program.")
            break
        elif a_list: 
            # Only add if the input is not empty (after strip)
            anime_list.append(a_list)
            print(f"Added '{a_list}'. Current list size: {len(anime_list)}")
        else:
            print("Please enter a valid anime name or 'exit'.")

    print("\nHere is the final list of animes:")
    if anime_list:
        for a in anime_list:
            print(f"- {a}")
    else:
        print("(The list is empty.)")

def challenge_15_prime_number_checker():
    """(WIP Implemented) Checks if a user-entered number is a prime number."""
    print("--- Code Challenge 15: Prime Number Checker ---")
    try:
        num = int(input("Enter a positive integer to check for primality: "))
        if num <= 1:
            print("The number must be greater than 1 to be prime.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    is_prime = True
    # Prime numbers are only divisible by 1 and themselves.
    # We only need to check divisibility from 2 up to the square root of the number.
    # For simplicity, we check up to num - 1.
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"\n✅ {num} IS a prime number.")
    else:
        print(f"\n❌ {num} is NOT a prime number.")
        
# --- Main Menu Functions ---

def display_menu(name: str):
    """Prints the main project menu to the console."""
    clear_screen()
    print(f"Hi! {name}!")
    print("\n|====================================================================|")
    print("|                        PYTHON PROJECT MENU                         |")
    print("|====================================================================|")
    
    # ACTIVITIES
    print("|                           ACTIVITIES (1-25)                        |")
    print("|--------------------------------------------------------------------|")
    # Using f-strings and list comprehension to keep the menu cleaner in the code
    activities = [
        "1. Hello World", "2. User Greeting", "3. Escape Sequences",
        "4. String/Len", "5. Data Type Check", "6. Arithmetic Ops",
        "7. Assignment Ops", "8. Comparison Ops", "9. Logical Ops",
        "10. Simple If/Else", "11. Elif Ladder", "12. Basic For Loop",
        "13. Accumulator Loop", "14. Countdown Loop", "15. Nested Box",
        "16. Right Triangle", "17. Inverted Triangle", "18. Right-Aligned Triangle",
        "19. Input Validation (New)", "20. List Manipulation (New)", 
        "21. Guessing Game", "22. While Loop Exit", "23. List/Reverse",
        "24. Dictionary Demo (New)", "25. Function Return (New)"
    ]
    
    # Format and print the activities in two columns
    for i in range(13):
        item1_index = i
        item2_index = i + 12
        
        item1_text = activities[item1_index] if item1_index < len(activities) else ""
        item2_text = activities[item2_index] if item2_index < len(activities) else ""
        
        # Add WIP annotation where appropriate
        # Note: Indices 18, 19, 23, 24 here refer to 19, 20, 24, 25 in activity number
        if item1_index == 18:
             item1_text += " (New/WIP)"
        if item1_index == 19:
             item1_text += " (New/WIP)"
        if item2_index == 23:
             item2_text += " (New/WIP)"
        if item2_index == 24:
             item2_text += " (New/WIP)"


        print(f"|    {item1_text:<30}{item2_text:<31}|")
    
    # CODE CHALLENGES
    print("|--------------------------------------------------------------------|")
    print("|                          CODE CHALLENGES (1-15)                    |")
    print("|--------------------------------------------------------------------|")
    
    challenges = [
        "1. ASCII Art", "2. Currency Breakdown", "3. Student Discount",
        "4. Manga Recommendator", "5. Factorial", "6. Fibonacci (New/WIP)",
        "7. Odd Accumulator", "8. Multiplication Table", "9. Spaceship Countdown",
        "10. Inverted Triangle", "11. Diamond Pattern", "12. Number Pyramid",
        "13. Odd Collector (While)", "14. List Collector (While)", "15. Prime Checker (New/WIP)"
    ]
    
    # Format and print challenges in two columns
    for i in range(8):
        item1_index = i
        item2_index = i + 8
        
        item1_text = challenges[item1_index] if item1_index < len(challenges) else ""
        item2_text = challenges[item2_index] if item2_index < len(challenges) else ""
        
        print(f"|    {item1_text:<30}{item2_text:<31}|")


    print("|--------------------------------------------------------------------|")
    print("||   0. Exit Program                                                ||")
    print("|====================================================================|")


def get_user_choice() -> Union[tuple[int, int], None]:
    """Handles user input for selecting an activity or challenge."""
    while True:
        print()
        try:
            choice_type = int(input("Do you want to run an ACTIVITY [1] or a CODE CHALLENGE [2]? (Type 1, 2, or 0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 0).")
            continue
            
        if choice_type == 0:
            return None # Signal to exit the main program
        
        elif choice_type == 1:
            try:
                b = int(input(f"Enter Activity number (1-{ACTIVITY_COUNT}): "))
                if 1 <= b <= ACTIVITY_COUNT:
                    return (1, b) # (Type, Number)
                else:
                    print(f"Invalid Activity number. Please enter a number between (1-{ACTIVITY_COUNT}).")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        elif choice_type == 2:
            try:
                c = int(input(f"Enter Code Challenge number (1-{CHALLENGE_COUNT}): "))
                if 1 <= c <= CHALLENGE_COUNT:
                    return (2, c) # (Type, Number)
                else:
                    print(f"Invalid Code Challenge number. Please enter a number between (1-{CHALLENGE_COUNT}).")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        else:
            print("Invalid Choice. Please type 1, 2, or 0.")

def run_selection(choice_type: int, number: int):
    """Maps the user's choice to the corresponding function and executes it."""
    clear_screen()
    
    # Dictionary mapping for Activities (Type 1)
    if choice_type == 1:
        activity_map = {
            1: activity_1_hello_world, 2: activity_2_user_greeting, 3: activity_3_escape_sequences,
            4: activity_4_string_methods_len, 5: activity_5_data_type_check, 6: activity_6_arithmetic_operators,
            7: activity_7_assignment_operators, 8: activity_8_comparison_operators, 9: activity_9_logical_operators,
            10: activity_10_simple_if_else, 11: activity_11_elif_ladder, 12: activity_12_basic_for_loop,
            13: activity_13_for_loop_accumulator, 14: activity_14_for_loop_countdown, 15: activity_15_nested_loops_simple_box,
            16: activity_16_nested_loops_right_triangle, 17: activity_17_nested_loops_inverted_right_triangle, 18: activity_18_nested_loops_pyramid_right_side,
            19: activity_19_while_loop_input_check, 20: activity_20_simple_list_manipulation, 21: activity_21_number_guessing_game,
            22: activity_22_while_loop_exit_control, 23: activity_23_list_iteration_and_reverse, 24: activity_24_simple_dictionary_usage,
            25: activity_25_function_with_return
        }
        
        func = activity_map.get(number)
        if func:
            func()
        else:
            print(f"Error: Activity {number} is not implemented or an error occurred.")

    # Dictionary mapping for Code Challenges (Type 2)
    elif choice_type == 2:
        challenge_map = {
            1: challenge_1_ascii_art, 2: challenge_2_currency_breakdown, 3: challenge_3_student_fare_discount,
            4: challenge_4_manga_recommendator, 5: challenge_5_factorial_calculator, 6: challenge_6_fibonacci_sequence_generator,
            7: challenge_7_odd_numbers_accumulator, 8: challenge_8_multiplication_table, 9: challenge_9_spaceship_countdown,
            10: challenge_10_inverted_triangle_pattern, 11: challenge_11_diamond_pattern, 12: challenge_12_number_pyramid_pattern,
            13: challenge_13_odd_number_collector, 14: challenge_14_list_input_collector, 15: challenge_15_prime_number_checker
        }
        
        func = challenge_map.get(number)
        if func:
            func()
        else:
            print(f"Error: Code Challenge {number} is not implemented or an error occurred.")

# --- Main Program Loop ---

def main():
    """The main entry point for the project menu application."""
    clear_screen()
    name = input("Please Enter your name ----> ").title().strip()
    
    if not name:
        name = "Guest"
        
    print(f"Hi! {name}! Welcome to {PROJECT_AUTHOR}'s Python Project Portfolio.")
    time.sleep(1)

    while True:
        display_menu(name)
        
        choice = get_user_choice()
        
        if choice is None:
            # Exit condition
            clear_screen()
            print("\nProgram terminated.")
            print(f"Thank you for checking my Program.\n")
            print(f"Developed by {PROJECT_AUTHOR} | Project Owner: {name}")
            break
        
        choice_type, number = choice
        
        try:
            run_selection(choice_type, number)
        except Exception as e:
            clear_screen()
            print(f"An unexpected error occurred during execution: {e}")
            
        pause()

if __name__ == "__main__":
    main()