task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no)? ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"High-priority task: {task}"
    case "medium":
        reminder = f"Medium-priority task: {task}"
    case "low":
        reminder = f"Low-priority task: {task}"
    case _:
        reminder = f"Task: {task} (priority not recognized)"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Provide a Customized Reminder
print(reminder)