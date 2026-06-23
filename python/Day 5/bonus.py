numbers=[]
for i in range(5):
    num=int(input("Enter the number:"))
    numbers.append(num)
largest = max(numbers)

smallest=min(numbers)

total = sum(numbers)
average = total / len (numbers)


print("largest number is ",largest)
print("smallest number is ",smallest)
print("sum of numbers is ",total)
print("Average is ", average)
