a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
op=input("Enter Operator (+, -, *, / and %): ")
addtion=a+b
sub=a-b
Devision=a/b
multipication=a*b
modulus=a%b

if op == "+":
    print("Addition Result: ",addtion)
elif op=="-":
    print("Subtraction Result: ", sub)
elif op=="*":
    print("Multipication Result:", multipication)
elif op=="/":
    print("Division:", Devision)
elif op=="%":
    print("Modulus Result: ", modulus)
else:
    print("Invalid Operator")