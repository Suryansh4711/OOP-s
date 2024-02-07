class Patient:
    def __init__(self, name, patient_id, age, gender, contact):
        self.__name = name
        self.__patient_id = patient_id
        self.__age = age
        self.__contact = contact
        self.__gender = gender

    def get_patientInfo(self):
        return {
            'patient_id': self.__patient_id,
            'name': self.__name,
            'age': self.__age,
            'Contact': self.__contact,
            'Gender': self.__gender
        }


class Doctor:
    def __init__(self, Id, name, specialisation):
        self.__name = name
        self.__specialisation = specialisation
        self.__id = Id

    def get_doctorInfo(self):
        return {
            'Id': self.__id,
            'Name': self.__name,
            'Specialisation': self.__specialisation
        }


class MedicalRecords:
    def __init__(self):
        self.__records = {}

    def add_records(self, patient, doctor, disease, medication):
        self.__records[patient.get_patientInfo()['patient_id']] = {'Patient': patient.get_patientInfo(),
                                                                   'Doctor': doctor.get_doctorInfo(),
                                                                   'Disease': disease,
                                                                   'Medication': medication}

    def get_records(self):
        return self.__records


# driver code
patient1 = Patient('Ravi', 1, 22, 'Male', '+916859745325')
patient2 = Patient('Rahul', 2, 19, 'Male', '+919785463254')
patient3 = Patient('Ravi', 3, 24, 'Male', '+916548547824')
patient4 = Patient('Rahul', 4, 25, 'Male', '+916582345782')
doctor1 = Doctor(3062, 'Dr. Karan', 'Cardiologist')
doctor2 = Doctor(6028, 'Dr. Arun', 'Surgeon')
# print(doctor1.get_doctorInfo(), doctor2.get_doctorInfo())
# print(patient1.get_patientInfo(), patient2.get_patientInfo())

record = MedicalRecords()
record.add_records(patient1, doctor1, 'Heart Problem', 'Aspirin')
record.add_records(patient2, doctor2, 'Cancer', 'Chemotherapy')
# print(record.get_records()[2])

name = input('Enter the name of the patient: ')
for i in record.get_records():
    if name == record.get_records()[i]['Patient']['name']:
        print(f"ID's for the requested patients is/are:\n {record.get_records()[i]['Patient']}")