import os

patients = []

# -------------------------
# Load Patients from File
# -------------------------
def load_patients():
    if os.path.exists("patients.txt"):
        with open("patients.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    patient = {
                        "id": data[0],
                        "name": data[1],
                        "age": data[2],
                        "disease": data[3]
                    }

                    patients.append(patient)


# -------------------------
# Save Patients to File
# -------------------------
def save_patients():
    with open("patients.txt", "w") as file:
        for patient in patients:
            file.write(
                patient["id"] + "," +
                patient["name"] + "," +
                patient["age"] + "," +
                patient["disease"] + "\n"
            )


load_patients()

while True:

    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # -------------------------
    # Add Patient
    # -------------------------
    if choice == "1":

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "disease": disease
        }

        patients.append(patient)

        save_patients()

        print("Patient Added Successfully!")

    # -------------------------
    # View Patients
    # -------------------------
    elif choice == "2":

        if len(patients) == 0:
            print("No patient records found.")

        else:

            print("\n===== Patient List =====")

            for patient in patients:

                print("----------------------------")
                print("Patient ID :", patient["id"])
                print("Name       :", patient["name"])
                print("Age        :", patient["age"])
                print("Disease    :", patient["disease"])

    # -------------------------
    # Search Patient
    # -------------------------
    elif choice == "3":

        search_id = input("Enter Patient ID: ")

        found = False

        for patient in patients:

            if patient["id"] == search_id:

                print("\n===== Patient Found =====")
                print("Patient ID :", patient["id"])
                print("Name       :", patient["name"])
                print("Age        :", patient["age"])
                print("Disease    :", patient["disease"])

                found = True
                break

        if not found:
            print("Patient not found.")

    # -------------------------
    # Update Patient
    # -------------------------
    elif choice == "4":

        update_id = input("Enter Patient ID to Update: ")

        found = False

        for patient in patients:

            if patient["id"] == update_id:

                patient["name"] = input("Enter New Name: ")
                patient["age"] = input("Enter New Age: ")
                patient["disease"] = input("Enter New Disease: ")

                save_patients()

                print("Patient Updated Successfully!")

                found = True
                break

        if not found:
            print("Patient not found.")

    # -------------------------
    # Delete Patient
    # -------------------------
    elif choice == "5":

        delete_id = input("Enter Patient ID to Delete: ")

        found = False

        for patient in patients:

            if patient["id"] == delete_id:

                patients.remove(patient)

                save_patients()

                print("Patient Deleted Successfully!")

                found = True
                break

        if not found:
            print("Patient not found.")

    # -------------------------
    # Exit
    # -------------------------
    elif choice == "6":

        print("Thank You!")
        break

    else:

        print("Invalid Choice! Please try again.")