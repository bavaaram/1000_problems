#Reading the number of sides and the length of each side of a regular polygon and calculating its area.

import math

num_side = int(input("Enter number of sides: "))
side_length = float(input("Enter length of each side: "))
pi = 3.1415926

area = ((num_side) * (side_length ** 2)) / (4 * math.tan((pi) / (num_side)))

print("The area of Regular polygon is %s" % str(area))
