x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
sign = input("Enter a mathematical operation(+,-,* or /): ")
if sign == '+':
    print(f"The sum is: {x+y}")
elif sign == '-':
    print(f"The difference is: {x-y}")
elif sign == '*':
    print(f"The product is: {x*y}")
elif sign == '/':
    print(f"The quotient is: {x/y}")
else:
    print("Enter a avlid operation")


  