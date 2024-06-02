# Class to represent a student with id, name, and career.
class Student:
    def __init__(self, name, id, career):
        self.name = name
        self.id = id
        self.career = career
    
    def setId(self, id):
        self.id = id
    
    def setName(self, name):
        self.name = name
    
    def setCareer(self, career):
        self.career = career
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getCareer(self):
        return self.career
    
    def __str__(self):
        return f"Student(id={self.id}, name={self.name}, career={self.career})"


# Class to represent a practice with a student, company, and duration.
class Practice:
    def __init__(self, student, company, duration):
        self.student = student
        self.company = company
        self.duration = duration
    
    def setStudent(self, student):
        self.student = student
    
    def setCompany(self, company):
        self.company = company
    
    def setDuration(self, duration):
        self.duration = duration
    
    def getStudent(self):
        return self.student
    
    def getCompany(self):
        return self.company
    
    def getDuration(self):
        return self.duration
    
    def __str__(self):
        return f"Practice(student={self.student}, company={self.company}, duration={self.duration})"


# Class to manage a collection of practices.
class PracticeManager:
    def __init__(self, size):
        self.practices = []
        self.size = size
        self.count = 0
    
    # Register a new practice if there is available space.
    def register(self, practice):
        if self.count < self.size:
            self.practices.append(practice)
            self.count += 1
        else:
            print("Cannot register more practices, maximum capacity reached.")
    
    # Calculate the average duration of all registered practices.
    def averageDuration(self):
        if self.count == 0:
            return 0
        total_duration = sum(p.getDuration() for p in self.practices)
        return total_duration / self.count
    
    # Count the number of practices in a given company.
    def countByCompany(self, company_name):
        return sum(1 for p in self.practices if p.getCompany() == company_name)
    
    # Change the company of a practice by student ID.
    def changeCompany(self, student_id, new_company):
        for practice in self.practices:
            if practice.getStudent().getId() == student_id:
                practice.setCompany(new_company)
    
    def __str__(self):
        return '\n'.join(str(practice) for practice in self.practices)


# Main class to interact with the user through a menu.
class PracticeSoft:
    def __init__(self, size):
        self.manager = PracticeManager(size)
    
    def main(self):
        while True:
            print("\nMenu:")
            print("1. Register a practice")
            print("2. Show the number of interns in a company")
            print("3. Show the average duration of practices")
            print("4. Change the company of a practice")
            print("5. Show all practices")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter student's name: ")
                id = input("Enter student's ID: ")
                career = input("Enter student's career: ")
                student = Student(name, id, career)
                company = input("Enter company name: ")
                duration = int(input("Enter practice duration (months): "))
                practice = Practice(student, company, duration)
                self.manager.register(practice)
            elif choice == '2':
                company = input("Enter company name: ")
                print(f"Number of interns in {company}: {self.manager.countByCompany(company)}")
            elif choice == '3':
                print(f"Average duration of practices: {self.manager.averageDuration()}")
            elif choice == '4':
                id = input("Enter student ID: ")
                new_company = input("Enter new company name: ")
                self.manager.changeCompany(id, new_company)
            elif choice == '5':
                print("All practices:")
                print(self.manager)
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    ps = PracticeSoft(10)
    ps.main()
