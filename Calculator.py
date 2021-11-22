def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Available operations:1)add 2)subtract 3)multiply 4)divide")
operation=input("Choose the operation(1,2,3,4): " )
if operation in ("1","2","3","4"):
    if operation == "1":
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print("Your addition is: ",add(x,y))
    elif operation == "2":
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print("Your subtraction is: ",subtract(x,y))
    elif operation == "3":
        x=float(input("Enter the first number: "))
        y=float(input("Enter the second number: "))
        print("Your multiplication is: ",multiply(x,y))
    elif operation == "4":
        x=float(input("Enter the dividend: "))
        y=float(input("Enter the divisor: "))
        print("Your quotient is: ",divide(x,y),"with remainder: ",x%y)
