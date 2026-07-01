#Highest mark

student = {
    "Rahul":90,
    "Fidha":95,
    "Asha":85
}
name = max(student , key=student.get)
print("Highest Scorer:",name)
print("Mark:", student[name])