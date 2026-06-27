
students = []
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input ("Enter your choice:")
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List")
            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("----------------")
    elif choice == "3":
        if len(students) == 0:
            print("No students found.")
        else:
            search_roll = input("Enter roll number to search: ")

            found = False

            for student in students:
                if student["roll"] == search_roll:
                    print("\nStudent Found")
                    print("Name:", student["name"])
                    print("Roll Number:", student["roll"])
                    found = True
                    break

            if not found:
                print("Student not found.")
    elif choice == "4":
        if len(students) == 0:
            print("No students found.")
        else:
            search_roll = input("Enter roll number to update: ")

            found = False

            for student in students:
                if student["roll"] == search_roll:

                    student["name"] = input("Enter new name: ")
                    student["roll"] = input("Enter new roll number: ")

                    print("Student updated successfully!")

                    found = True
                    break

            if not found:
                print("Student not found.")
    elif choice == "5":
        if len(students) == 0:
            print("No students found.")
        else:
            search_roll = input("Enter roll number to delete: ")
  
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
        print("Thank you!")
        break
    else:
        print("Invalid choice.")