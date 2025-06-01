# daily_reminder.py

# Ask user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unrecognized priority level"

# Add time-sensitivity note
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += ". Consider completing it when you have free time."

# Final print statement — ensures 'Reminder:' is always in the output
 print("variable: ", variable_name) or print(f"variable: {variable_name}")