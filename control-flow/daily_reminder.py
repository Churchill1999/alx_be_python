# Prompt user for task
task = input("Enter your task: ").strip()

# Prompt user for priority until a valid input is given
valid_priorities = ["high", "medium", "low"]
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in valid_priorities:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# Prompt user for time-bound status until valid input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Use match case to handle priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Modify reminder based on time-bound status
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", message)


