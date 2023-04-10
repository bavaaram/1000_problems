#Refer to the explanation of Problem 0007 in the relevant book.
one_molecule = 3 * (10 ** -23)         #gram per unit
lit = float(input("Enter Volume in Liter: "))
w = 950        #gram per liter
nums = (lit * w) / one_molecule
print("The number of Molecules in %s Liter Water is %s" % (lit, nums)) 
