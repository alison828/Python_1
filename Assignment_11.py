
# Ask user to input a positive number

user_input = input( "Enter a positive number: ")

# Check if the user entered a positive number
while not user_input.isdigit() or int(user_input) <= 0:
    user_input = input("Invalid input. Please enter a positive number: ")

# Convert the user input to int
number = int(user_input)

# We will be generating the collatz sequence steps below

sequence = []
while number != 1:
    sequence.append(number)
    if number % 2 == 0: # an expression to identify if the number is even
        number //= 2 # expresssion to divide the number by 2

    else: # if its odd then multiply by 3 and add plus 1
        number = 3 * number + 1


    # Add one at the end of the sequence
sequence.append(1)

print("The Collatz sequence is: " , sequence)









