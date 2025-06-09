import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=days)
    print("Future date after", days, "days:", future_date.strftime("%Y-%m-%d"))

# Run the functions
display_current_datetime()

try:
    user_input = int(input("Enter the number of days to add: "))
    calculate_future_date(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")