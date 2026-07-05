import os

employees = []

# ----------------------------
# Load Employees from File
# ----------------------------
def load_employees():
    if os.path.exists("employees.txt"):
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    employees.append({
                        "id": data[0],
                        "name": data[1],
                        "department": data[2],
                        "salary": data[3]
                    })


# ----------------------------
# Save Employees to File
# ----------------------------
def save_employees():
    with open("employees.txt", "w") as file:
        for employee in employees:
            file.write(f"{employee['id']},{employee['name']},{employee['department']},{employee['salary']}\n")


load_employees()

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ----------------------------
    # Add Employee
    # ----------------------------
    if choice == "1":

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")

        employees.append({
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        })

        save_employees()

        print("Employee Added Successfully!")

    # ----------------------------
    # View Employees
    # ----------------------------
    elif choice == "2":

        if len(employees) == 0:
            print("No employees found.")

        else:
            print("\n===== Employee List =====")

            for employee in employees:

                print("-------------------------")
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Department  :", employee["department"])
                print("Salary      :", employee["salary"])

    # ----------------------------
    # Search Employee
    # ----------------------------
    elif choice == "3":

        search_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:

            if employee["id"] == search_id:

                print("\n===== Employee Found =====")
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Department  :", employee["department"])
                print("Salary      :", employee["salary"])

                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Update Employee
    # ----------------------------
    elif choice == "4":

        update_id = input("Enter Employee ID to Update: ")

        found = False

        for employee in employees:

            if employee["id"] == update_id:

                employee["name"] = input("Enter New Name: ")
                employee["department"] = input("Enter New Department: ")
                employee["salary"] = input("Enter New Salary: ")

                save_employees()

                print("Employee Updated Successfully!")

                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Delete Employee
    # ----------------------------
    elif choice == "5":

        delete_id = input("Enter Employee ID to Delete: ")

        found = False

        for employee in employees:

            if employee["id"] == delete_id:

                employees.remove(employee)

                save_employees()

                print("Employee Deleted Successfully!")

                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")