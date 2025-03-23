# Represents an elderly person with health and medication details.
class ElderlyPerson:
    
    def __init__(self, name, age, health_condition):
        self.name = name
        self.age = age
        self.health_condition = health_condition
        self.medication_history = []

    # Adds a medication record to the person's history.
    def add_medication(self, medication_name, dosage, date):
        self.medication_history.append({
            'medication_name': medication_name,
            'dosage': dosage,
            'date': date
        })

    # Returns the medication history of the person.
    def get_medication_history(self):
        return self.medication_history

    # Returns a string representation of the elderly person.
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Health Condition: {self.health_condition}"


# Manages a collection of elderly persons.
class ElderlyCareModel:
    
    def __init__(self):
        self.elderly_persons = []

    # Adds a new elderly person to the system.
    def add_elderly_person(self, name, age, health_condition):
        person = ElderlyPerson(name, age, health_condition)
        self.elderly_persons.append(person)
        return person

    # Retrieves an elderly person by their name.
    def get_elderly_person_by_name(self, name):
        for person in self.elderly_persons:
            if person.name == name:
                return person
        return None

    # Returns a list of all elderly persons.
    def get_all_elderly_persons(self):
        return self.elderly_persons