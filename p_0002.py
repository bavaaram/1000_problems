#Calculate the volume and area of the cylinder by reading its radius and height.
radius = float(input("Enter Radius of cylinder: "))
height = float(input("Enter Height of cylinder: "))
pi = 3.1415926
volume = pi * height *(radius ** 2)
area = (2 * pi * radius * height) + (2 * (pi * (radius ** 2)))

print("Volume is: %f" % volume)
print("Area is: %f" % area)
