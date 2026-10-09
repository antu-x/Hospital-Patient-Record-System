# Hospital Patient Record System

patients = []

while True:

    print("\n===== Hospital Patient Record System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Patient
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

        print("Patient added successfully!")

    # View Patients
    elif choice == "2":

        if len(patients) == 0:
            print("No patient records found.")

        else:
            print("\n--- Patient Records ---")

            for patient in patients:
                print("Patient ID:", patient["id"])
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                print("----------------------")

    # Search Patient
    elif choice == "3":

        search_id = input("Enter Patient ID: ")

        for patient in patients:

            if patient["id"] == search_id:
                print("\nPatient Found!")
                print("Patient ID:", patient["id"])
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                break

        else:
            print("Patient not found.")

    # Exit
    elif choice == "4":

        print("Thank you!")
        break

    else:

        print("Invalid choice!")