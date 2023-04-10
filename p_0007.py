#A program that reads two numbers and displays the complex equivalent of those two numbers. The first number read is the real part. The second number is an imaginary part. The goal is to create complex numbers and display them.

a = float(input("Enter the Real Parameter: "))
b = float(input("Enter the Imaginary Parameter: "))

res = complex(a, b)

print("The Result is %s" % str(res))
