
       #BASIC CALCULATOR

num1=int(input("enter a number:"))
operator=input("enter operator(+,-,/,*,//,%):")
num2=int(input("enter 2nd number:"))
if operator == '+':
    print("addition=",num1+num2)
elif operator == '-':
    print("subtraction=",num1-num2)
elif operator == '*':
    print("MUltiplication=",num1*num2)
elif operator == '/':
    print("Division=",num1/num2)
elif operator == '//':
    print("Floor value",num1//num2)
elif operator == '%':
    print("REmainder",num1%num2)
else:
    print("invalid error:")

print("-----------PROGRAM--EXIT------------")