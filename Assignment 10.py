



#promt the user for their age

age = input( "Please enter your age: ")

# Process the data and check the input

if age.isdigit():
    age = int(age)

    if age > 0:
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("Adult")

        else:
            print("Senior Citizen")
    else:
        print("Error: Age must be positive integer value")
else:
    print( "Error: Invalid input,  Please enter a positive number")






