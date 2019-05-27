num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
num3=int(input("Enter a number3: "))
if((num1>num2)&(num1>num3)):
    print(num1,"is a gretest")
elif((num2>num3)&(num2>num1)):
    print(num2,"is a gretest")
else:
    print(num3,"is a gretest")
input("press enter to exit")
