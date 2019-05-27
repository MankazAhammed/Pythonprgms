num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
try:
    num3=num1/num2
except:
    print("you can/'t divide any number with zero")
else:
    print(num3)
