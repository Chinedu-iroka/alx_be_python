import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted date/time:", formatted)

def calculate_future_date(days):
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Prompt the user
try:
    user_input = int(input("Enter number of days: "))
    calculate_future_date(user_input)
except ValueError:
    print("Please enter a valid integer.")