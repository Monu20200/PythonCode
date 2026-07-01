num1 = float(input("enter the num 1: "))
num2 = float(input("enter the num 2: "))
num3 = float(input("enter the num 3: "))
num4 = float(input("enter the num 4: "))
if num1> num2 and num1>num3 and num1>num4:
    print(num1,"is greatest")
elif num2>num3 and num2>num4:
    print(num2,"is greatest")
elif num3>num4:
    print(num3,"is greatest")
else:
    print(num4,"is greatest")
