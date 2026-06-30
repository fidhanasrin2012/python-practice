#Multiplication table using function


def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

number = int(input("Enter a number: "))
table(number)