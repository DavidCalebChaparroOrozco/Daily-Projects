# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Person (Patient and Doctor)
class Person(ABC):
    def __init__(self, name, id_number):
        # Encapsulation: Making attributes private
        self._name = name
        self._id_number = id_number

    @abstractmethod
    def get_description(self):
        """
        Abstract method to get the description of the person.
        Subclasses must implement this method.
        """
        pass

    # Getter method to retrieve the name of the person
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person
    def get_id_number(self):
        return self._id_number


# Inheritance for Patient
class Patient(Person):
    def __init__(self, name, id_number, age):
        super().__init__(name, id_number)
        self._age = age
        self._appointments = []

    # Implement the abstract method to get the description of the patient
    def get_description(self):
        return f"Patient: {self.get_name()} (ID: {self.get_id_number()}, Age: {self._age})"

    # Method to add an appointment for the patient
    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    # Method to get the list of appointments for the patient
    def get_appointments(self):
        return self._appointments


# Inheritance for Doctor
class Doctor(Person):
    def __init__(self, name, id_number, specialty):
        super().__init__(name, id_number)
        self._specialty = specialty
        self._patients = []

    # Implement the abstract method to get the description of the doctor
    def get_description(self):
        return f"Doctor: {self.get_name()} (ID: {self.get_id_number()}, Specialty: {self._specialty})"

    # Method to add a patient to the doctor's list
    def add_patient(self, patient):
        self._patients.append(patient)

    # Method to get the list of patients under the doctor
    def get_patients(self):
        return self._patients


# Class for Appointment
class Appointment:
    def __init__(self, patient, doctor, date, time, reason):
        self._patient = patient
        self._doctor = doctor
        self._date = date
        self._time = time
        self._reason = reason

    # Method to get the appointment details
    def get_details(self):
        return (f"Appointment for {self._patient.get_name()} with Dr. {self._doctor.get_name()} "
                f"on {self._date} at {self._time} for {self._reason}")


# Function to display the menu
def display_menu():
    print("\nMedical Appointment System")
    print("1. Register new patient")
    print("2. Register new doctor")
    print("3. Schedule a new appointment")
    print("4. Display patient details")
    print("5. Display doctor details")
    print("6. Exit")
    print("=".center(50, "="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Dictionary to hold patients
    patients = {}

    # Dictionary to hold doctors
    doctors = {}

    while True:
        option = display_menu()

        if option == "1":
            # Register new patient
            patient_name = input("Enter patient name: ")
            patient_id = input("Enter patient ID: ")
            patient_age = int(input("Enter patient age: "))
            if patient_id not in patients:
                patients[patient_id] = Patient(patient_name, patient_id, patient_age)
                print("Patient registered successfully.")
            else:
                print("Patient ID already exists.")

        elif option == "2":
            # Register new doctor
            doctor_name = input("Enter doctor name: ")
            doctor_id = input("Enter doctor ID: ")
            specialty = input("Enter doctor's specialty: ")
            if doctor_id not in doctors:
                doctors[doctor_id] = Doctor(doctor_name, doctor_id, specialty)
                print("Doctor registered successfully.")
            else:
                print("Doctor ID already exists.")

        elif option == "3":
            # Schedule a new appointment
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            if patient_id in patients and doctor_id in doctors:
                date = input("Enter appointment date (YYYY-MM-DD): ")
                time = input("Enter appointment time (HH:MM): ")
                reason = input("Enter reason for appointment: ")
                patient = patients[patient_id]
                doctor = doctors[doctor_id]
                appointment = Appointment(patient, doctor, date, time, reason)
                patient.add_appointment(appointment)
                doctor.add_patient(patient)
                print("Appointment scheduled successfully.")
            else:
                print("Patient or Doctor ID not found.")

        elif option == "4":
            # Display patient details
            patient_id = input("Enter patient ID: ")
            if patient_id in patients:
                patient = patients[patient_id]
                print(patient.get_description())
                for appointment in patient.get_appointments():
                    print(f" - {appointment.get_details()}")
            else:
                print("Patient not found.")

        elif option == "5":
            # Display doctor details
            doctor_id = input("Enter doctor ID: ")
            if doctor_id in doctors:
                doctor = doctors[doctor_id]
                print(doctor.get_description())
                for patient in doctor.get_patients():
                    print(f" - {patient.get_description()}")
            else:
                print("Doctor not found.")

        elif option == "6":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")
