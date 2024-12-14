
# Prompt the user for weight and height
Weight_input = input("Enter the weight in kg: ")
Height_input = input("Enter your height in meters: ")

#convert the input to a float

weight = float(Weight_input)
height = float(Height_input)

# calculate BMI

bmi = weight / (height ** 2)

#Display the output
print("your BMI is: ", bmi)






