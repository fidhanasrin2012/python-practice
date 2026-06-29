#Count even and odd numbers

numbers = [10, 15, 22, 37, 48]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)