#A program that reads an employee's salary and calculates and displays his insurance, taxes and receipts. Insurance and tax are assumed to be 6 and 10 percent of the employee's salary, respectively.

salary = int(input("Enter your Salary: "))

tax = salary * -1.1
insurance = salary * -1.07

absolute_salary = salary - tax - insurance

print("Absolute Slary is %s" % str(absolute_salary))
print("The Taxes Fee is %s" % str(tax))
print("The Insurance Fee is %s" % str(insurance))
