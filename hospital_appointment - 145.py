def Hospital():
    print("\nAll available Doctors:")
    doctors = {"John": "Cardio", "Smith": "Physio", "Harry": "ENT", "Rowling": "Vascular"}
    
    for doc, spec in doctors.items():
        print(f"Dr.{doc} - {spec}")

    user_choice = input("\nSelect doctor or speciality: ").capitalize()

    availability = {
        "John": "Tuesday",
        "Smith": "Monday",
        "Harry": "Wednesday",
        "Rowling": "Thursday"
    }

    if user_choice in doctors:
        print(f"Doctor available on: {availability[user_choice]}")
    elif user_choice in doctors.values():
        for doc, spec in doctors.items():
            if spec.lower() == user_choice.lower():
                print(f"{doc} is available on {availability[doc]}")
                user_choice = doc
    else:
        print("Invalid choice")
        return

    choice = input("\nEnter speciality needed: ").capitalize()
    day = input("Enter day: ").capitalize()
    user_id = int(input("Enter user id: "))

    slot_book(choice, day, user_id, user_choice)


def slot_book(choice, day, user_id, doctor):
    availability = {
        "John": "Tuesday",
        "Smith": "Monday",
        "Harry": "Wednesday",
        "Rowling": "Thursday"
    }

    if availability.get(doctor) == day:
        print("Slot available!")
        action = input("Enter book/reschedule/cancel: ").lower()

        if action == "book":
            print(f"Booked with Dr.{doctor} on {day}")
            consultation(user_id)

        elif action == "reschedule":
            print("Restart booking...")
            Hospital()

        elif action == "cancel":
            print("Appointment cancelled.")

    else:
        print("Doctor not available on this day.")


def patient_details(name, age, contact, user_id):
    print("\nPatient Registered Successfully!")
    print(f"Name: {name}, Age: {age}, Contact: {contact}, ID: {user_id}")


def consultation(user_id):
    print(f"\nMedical ID: {user_id}")
    print("Prescription: Take rest and stay hydrated.")


# MAIN
print("------ Welcome to SK Hospitals ------")

print("\n1) New User")
print("2) Book Appointment")

user = int(input("Enter choice: "))

if user == 1:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    contact = input("Enter contact: ")
    user_id = int(input("Enter ID: "))
    patient_details(name, age, contact, user_id)
    Hospital()

elif user == 2:
    user_id = int(input("Enter ID: "))
    Hospital()