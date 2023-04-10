#Reading the number of sides and the length of each side of a regular polygon and calculating its area.

from math import tan, pi

num_side = int(input("Enter number of sides: "))
side_length = float(input("Enter length of each side: "))

area = ((num_side) * (side_length ** 2)) / (4 * tan((pi) / (num_side)))

print("The area of Regular polygon is %s" % str(area))
