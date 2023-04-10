#A program that reads a string and the number of repetitions and repeats and displays the string by the number of entered numbers.

s = input("Enter a string: ")
rep = int(input("Enter the number of repeats: "))

res = s * rep

print("The result is %s" % res)
