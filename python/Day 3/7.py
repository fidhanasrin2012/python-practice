#Find the factorial of a number

num = int (input("Enter the number:"))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial * i
print ("Factorial =", factorial)


#while loop

num = int (input("Enter the number:"))
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i= i+1
print ("Factorial =", factorial)

