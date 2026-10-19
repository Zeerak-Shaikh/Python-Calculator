import math

operator = input('Enter the operator(+-*/):')
a =float(input("Enter the first number:"))
b =float(input("Enter the Second Number:"))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator== "/":
    print(a/b)
else:
    print("Enter a valid operator")

