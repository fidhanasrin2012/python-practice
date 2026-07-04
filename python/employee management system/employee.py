employees = []

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # -------------------------
    # Add Employee
    # -------------------------
    if choice == "1":

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        }

        employees.append(employee)

        print("Employee Added Successfully!")

    # -------------------------
    # View Employees
    # -------------------------
    elif choice == "2":

        if len(employees) == 0:
            print("No employees found.")

        else:

            print("\n===== Employee List =====")

            for employee in employees:

                print("----------------------------")
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Department  :", employee["department"])
                print("Salary      :", employee["salary"])

    # -------------------------
    # Search Employee
    # -------------------------
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

    # -------------------------
    # Exit
    # -------------------------
    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice! Please try again.")