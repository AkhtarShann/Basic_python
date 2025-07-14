# Data Structures in Python

# 1. List (Mutable)
my_list = [1, "str", True]

# 2. Tuple (Immutable)
my_tuple = (1, "str", True)

# 3. Set (Unique and Unordered)
my_set = {1, 2, 3, 2, 1}  # Duplicates will be removed

# 4. Dictionary (Key-Value Pairs)
student = {
    "name": "Ali",
    "age": 20
}
print(student)



def student_info(name, age=18, *args, **kwargs):
    print("Name:", name)
    print("Age:", age)
    print("Additional positional arguments (args):", args)
    print("Additional keyword arguments (kwargs):", kwargs)



# Call the function
student_info(
    "Ali",                # regular argument
    20,                   # overriding default argument
    "Rawalpindi", "BSCS",     # *args (extra values)
    roll_no=40211, dept="CS"  # **kwargs (extra key-value pairs)
)




# Decorator to check PIN before allowing access
def pin_required(correct_pin):
    def decorator(func):
        def wrapper(pin_entered):
            if pin_entered == correct_pin:
                return func()
            else:
                print("Access denied! Incorrect PIN.")
        return wrapper
    return decorator

# Function protected by PIN
@pin_required("1234")
def access_system():
    print("Access granted! Welcome to the system.")

# Example usage
user_pin = input("Enter your PIN: ")
access_system(user_pin)

import datetime

import time



# Decorator to measure function execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper




# Function that simulates some processing
@timing_decorator
def process_data():
    print("Processing data...")
    time.sleep(2)  # Simulate a delay (like downloading, computation)
    print("Done!")

# Example usage
process_data()




# Decorator to check user authentication
def require_authentication(is_authenticated):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_authenticated:
                return func(*args, **kwargs)
            else:
                print("Access denied! Please login first.")
        return wrapper
    return decorator

# Simulate user login status
user_logged_in = True  # Change to False to test access denied

@require_authentication(user_logged_in)
def view_dashboard():
    print("Welcome to your dashboard!")

# Example usage
view_dashboard()



# Iterator using a class
class MyIterator:
    print("Iterator")
    def __init__(self, max_val):
        self.max = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration



# Using the iterator
it = MyIterator(5)
for num in it:
    print(num)



# Generator using yield
def my_generator(max_val):
    print("Generator")
    current = 0
    while current < max_val:
        yield current
        current += 1

# Using the generator
for num in my_generator(5):
    print(num)
