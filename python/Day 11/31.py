#Linear search

numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

if key in numbers:
    print("Element Found")
else:
    print("Element Not Found")