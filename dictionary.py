"""this is an in class exercise
"""


def create_patient_entry(first_name, last_name, id, age):
    """create a patient entry"""
    new_patient = {
        "First Name": first_name,
        "Last Name": last_name,
        "ID": id,
        "Age": age,
        "Tests": [],
    }
    return new_patient


def full_name(patient):
    """return the full name"""
    return patient["First Name"] + " " + patient["Last Name"]


def find_patient(database, id):
    """find a patient"""
    patient = database[id]
    return patient


def print_database(database):
    """print the database"""
    for patient in database:
        print(patient)
        print(
            "First Name:{},ID:{},Age:{} ".format(
                full_name(patient), patient["ID"], patient["Age"]
            )
        )


def add_test_to_patient(database, id, test_name, test_value):
    """add a test to a patient"""
    patient = find_patient(database, id)
    patient["Tests"].append((test_name, test_value))


def adult_or_child(patient):
    """return adult or child"""
    if patient["Age"] >= 18:
        return "Adult"
    return "Child"


def main():
    """main function"""
    database = {}
    database[1] = create_patient_entry("John", "Smith", 1, 20)
    database[2] = create_patient_entry("Jane", "Doe", 2, 30)
    database[3] = create_patient_entry("John", "Doe", 3, 40)
    print_database(database)
    # print("Patient {} is a {}").format(
    #    full_name(database[0]), adult_or_child(database[0])
    # )


if __name__ == "__main__":
    main()
