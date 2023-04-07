#Calculate the volume and area of the sphere by reading its radius.
pi = 3.1415926
radius = float(input("Enter Radius of cylinder: "))

volume = 4 / 3 * (pi * (radius ** 3))
area = 4 * pi * (radius ** 2)

print("Volume is: %f" % volume)
print("Area is: %f" % area)
