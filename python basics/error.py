try:
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
        result = num1 / num2print("result is", result)
except ZeroDivisionError:
    print("division by zero is error !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
except ValueError:
    print("plese enter the entire number")
except:
    print("wrong input")
else:
    print("wrong exceptions")
finally:
    print("this will work")
