
def convert_time_duration():
    while True:  # Keep prompting the user until valid input is provided
        try:
            # Input: Prompt the user to enter a time duration in hours
            hours = float(input("Enter time duration in hours (non-negative number): "))

            # Check if the input is non-negative
            if hours < 0:
                raise ValueError("Time duration must be a non-negative number.")

            # Processing: Convert hours to minutes and seconds
            minutes = hours * 60
            seconds = minutes * 60

            # Output: Display the results
            print(f"{hours} hours is equal to {int(minutes)} minutes and {int(seconds)} seconds.")
            break  # Exit the loop after successful input and conversion

        except ValueError as e:
            # Handle invalid input and display error message
            print(f"Invalid input: {e}. Please try again.")

# Call the function
convert_time_duration()













