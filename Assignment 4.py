

x1 = float(input( "enter x1 coordinates: "))
x2 = float(input( "Enter x2 coordinates: "))
y1 = float(input( "Enter y1 coordinates: "))
y2 = float(input( "Enter y2 coordinates: "))

#calculation below

dx_squared = (x2 - x1) ** 2
dy_squared = (y2 - y1) ** 2

#calculate the distance square

distance_squared = dx_squared + dy_squared

#calculate the actual distance for the square feet

distance = distance_squared ** 0.5

#output the results
print( "The distance between the point is: ", distance)












