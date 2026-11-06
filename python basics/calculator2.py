num1=float(input("enter the 1st number:"))
num2=float(input("enter the 2nd number:"))
print("choose operation: , +, -, * , /")
operation = input("print operation")
if operation == '+':
    print("result:", num1 + num2)
elif operation == '-':
    print("result:", num1 - num2)
elif operation == '*':
    print("result:", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("u cant divide a number by 0!")
    else:
        print("result:", num1 / num2)
else:
    print("wrong operation")
    
