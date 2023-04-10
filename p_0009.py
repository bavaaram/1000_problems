#A program that receives the age from the user and converts it to seconds.
sec = 3.156 * (10 ** 7)         #Seconds per Year
age = int(input("Enter your Age: "))
res = age * sec

print("Your age in seconds is %s" % res)
