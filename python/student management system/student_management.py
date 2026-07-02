students =[]

try:
    file = open("students.txt", "r")

    while True:
        name = file.readline().strip()

        if not name:
            break

        roll = file.readline().strip()
        department = file.readline().strip()
        cgpa = file.readline().strip()

        file.readline()   # Skip separator line

        student = {
            "name": name.replace("Name: ", ""),
            "roll": roll.replace("Roll Number: ", ""),
            "department": department.replace("Department: ", ""),
            "cgpa": cgpa.replace("CGPA: ", "")
        }

        students.append(student)

    file.close()

except FileNotFoundError:
    pass
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        department = input("Enter Department: ")
        cgpa = input("Enter CGPA: ")

        student = {
            "name": name,
            "roll": roll,
            "department": department,
            "cgpa": cgpa
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:

            print("\n===== Student List =====")

            for student in students:

                print("-------------------------")
                print("Name       :", student["name"])
                print("Roll No    :", student["roll"])
                print("Department :", student["department"])
                print("CGPA       :", student["cgpa"])

    elif choice == "3":

        if len(students) == 0:
            print("No students found.")

        else:
            search_name = input("Enter Student Name: ").lower()

            found = False

            for student in students:

                if student["name"].lower() == search_name:

                    print("\n===== Student Found =====")
                    print("Name       :", student["name"])
                    print("Roll No    :", student["roll"])
                    print("Department :", student["department"])
                    print("CGPA       :", student["cgpa"])

                    found = True
                    break

            if not found:
                print("Student not found.")
    

    elif choice == "4":

        search_roll = input("Enter Roll Number to Update: ")

        found = False

        for student in students:

            if student["roll"] == search_roll:

                student["name"] = input("Enter New Name: ")
                student["roll"] = input("Enter New Roll Number: ")
                student["department"] = input("Enter New Department: ")
                student["cgpa"] = input("Enter New CGPA: ")

                print("Student updated successfully!")

                found = True
                break

        if not found:
            print("Student not found.")
    
    elif choice == "5":

        search_roll = input("Enter Roll Number to Delete: ")

        found = False

        for student in students:

            if student["roll"] == search_roll:

                students.remove(student)

                print("Student deleted successfully!")

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "6":

        file = open("students.txt", "w")

        for student in students:

            file.write("Name: " + student["name"] + "\n")
            file.write("Roll Number: " + student["roll"] + "\n")
            file.write("Department: " + student["department"] + "\n")
            file.write("CGPA: " + student["cgpa"] + "\n")
            file.write("--------------------------\n")

        file.close()
 
        print("Student data saved successfully!")


    elif choice == "7":

        print("Total Students:", len(students))

    elif choice == "8":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")