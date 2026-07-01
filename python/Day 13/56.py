#Sort dictionary by key

student = {
    "Rahul":90,
    "Fidha":95,
    "Asha":85
}

sorted_dict = sorted(student.items(),key=lambda x: x[1])
for i in sorted_dict:
    print(i)