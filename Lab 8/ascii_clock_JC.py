# Prompt the user to enter a time and store it in a variable
user_time = input("Enter the time: ")
# Prompt the user to enter the clock type and store it in a variable
clock_type = input("Enter the clock type (12 or 24): ")
# Use conditional statements to convert the time accordingly
if clock_type == "12":
    # Convert the time to 12-hour format
    # Split the time into hours and minutes
    time_parts = user_time.split(":")
    # Get the hour and minute values
    hour = int(time_parts[0])
    minute = time_parts[1]
    # If the hour is greater than 12, subtract 12 and set the period to PM, otherwise set it to AM
    if hour > 12:
        hour -= 12
        period = "PM"
    else:
        period = "AM"
    converted_time = f"{hour}:{minute} {period}"
elif clock_type == "24":
    # Convert the time to 24-hour format
    time_parts = user_time.split(":")
    # Get the hour and minute values
    hour = int(time_parts[0])
    minute = time_parts[1]
    # If the hour is less than 12, set the period to AM, otherwise set it to PM
    if hour < 12:
        period = "AM"
    else:
        # (Hour is 12)
        period = "PM"
    converted_time = f"{hour}:{minute} {period}"
else:
    converted_time = "Invalid clock type entered."
# Prompt the user to enter the preferred character
pref_char = input("Enter your preferred character: ")
# Use if statement to ensure validity of the preferred character
if pref_char not in "abcdeghkmnopqrsuvwxyz@$&*=" and pref_char != " ":
    while pref_char not in "abcdeghkmnopqrsuvwxyz@$&*=":
        pref_char = input("Character not permitted! Try again: ")
# Now we need to determine the pref char if the user entered a space
