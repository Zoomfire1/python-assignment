patients = {
    101: {'Name': 'John Doe', 'Age': 45, 'Disease': 'Hypertension'},
    102: {'Name': 'Jane Smith', 'Age': 38, 'Disease': 'Diabetes'},
    103: {'Name': 'Emily Johnson', 'Age': 60, 'Disease': 'Arthritis'}
}


def display_patient_details(patient_id):
    
    if patient_id in patients:
        details = patients[patient_id]
        print(f"Patient ID: {patient_id}")
        print(f"Name    : {details['Name']}")
        print(f"Age     : {details['Age']}")
        print(f"Disease : {details['Disease']}")
          
    else:
        print(f"No patient found with ID {patient_id}")
    


patient_id = int(input("Enter the patient ID: "))
display_patient_details(patient_id)
