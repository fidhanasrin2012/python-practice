a=int(input("Enter the First number:"))
b=int(input("Enter the Second number:"))
op = input ("Enter the operator(+,-,*,/):")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print ("Invalid Operator")