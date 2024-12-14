
# Define the character for the pattern and the number of rows
pattern_char = "*" # You can change this to any character
num_rows = 7       # Change this to the desired number of rows

# Generate the pattern using nested loops
print("Generated Pattern: ")
for i in range (1, num_rows + 1):
    for j in range (i) :
        print (pattern_char, end="")
    print() # move to the next line after each row









