#A program that reads the wind speed at a height of 10 meters in meters per second and reads the air temperature in degrees Celsius and calculates the Wind Chill index.

import math

velocity = float(input("Enter the velocity at 10 meter height in m/s: "))
temp = float(input("Enter the temperature in celcius degree: "))

w_chill = 13.12 + (temp * 0.6215) - (11.37 * (velocity ** 0.16)) + (0.3965 * temp * (velocity ** 0.16))

print("The Wind Chill Index is %s" % str(w_chill))
