#Find common elements in two lists

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print(common)