#count the number of digits in a number

num = int (input("Enter the number:"))
count =0
while num >0:
    num = num // 10
    count = count + 1
print ("number of digits",count)
