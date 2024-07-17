# Importing necessary libraries
from abc import ABC, abstractmethod

# Base Class for Person (Student and Teacher)
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

    # Getter method to retrieve the name of the person.
    def get_name(self):
        return self._name

    # Getter method to retrieve the ID number of the person.
    def get_id_number(self):
        return self._id_number


# Inheritance for Student
class Student(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._courses = []

    # Implement the abstract method to get the description of the student.
    def get_description(self):
        return f"Student: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to enroll in a course.
    def enroll_course(self, course):
        self._courses.append(course)

    # Method to get the list of courses the student is enrolled in.
    def get_courses(self):
        return self._courses


# Inheritance for Teacher
class Teacher(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        self._courses = []

    # Implement the abstract method to get the description of the teacher.
    def get_description(self):
        return f"Teacher: {self.get_name()} (ID: {self.get_id_number()})"

    # Method to assign a course to the teacher.
    def assign_course(self, course):
        self._courses.append(course)

    # Method to get the list of courses the teacher is teaching.
    def get_courses(self):
        return self._courses


# Class for Course
class Course:
    def __init__(self, name, credits, teacher, max_students):
        self._name = name
        self._credits = credits
        self._teacher = teacher
        self._max_students = max_students
        self._students = []

    # Method to get the description of the course.
    def get_description(self):
        return f"Course: {self._name} ({self._credits} credits), Teacher: {self._teacher.get_name()}"

    # Method to add a student to the course.
    def add_student(self, student):
        if len(self._students) < self._max_students:
            self._students.append(student)
            return True
        else:
            return False

    # Method to get the total students in the course.
    def get_total_students(self):
        return len(self._students)

    # Method to get the total cost for a student based on the credits.
    def get_total_cost(self):
        return self._credits * 100  # Assuming each credit costs $100


# Function to print course details
def print_course_details(course):
    print(course.get_description())
    print(f"Total students: {course.get_total_students()}")
    print(f"Total cost per student: ${course.get_total_cost():.2f}")


# Function to display the menu
def display_menu():
    print("\nUniversity Enrollment System")
    print("1. Enroll a student in a course")
    print("2. Display student details")
    print("3. Display course details")
    print("4. Exit")
    print("=".center(50,"="))
    return input("Select an option: ")


# Main code
if __name__ == "__main__":
    # Create instances of teachers
    teacher1 = Teacher("Dr. Smith", "T001")
    teacher2 = Teacher("Dr. Johnson", "T002")

    # Create instances of courses
    course1 = Course("Mathematics", 3, teacher1, 30)
    course2 = Course("Physics", 4, teacher2, 25)

    # Assign courses to teachers
    teacher1.assign_course(course1)
    teacher2.assign_course(course2)

    # Dictionary to hold students
    students = {}

    while True:
        option = display_menu()

        if option == "1":
            # Enroll a student in a course
            student_name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            course_name = input("Enter course name (Mathematics/Physics): ")

            if student_id not in students:
                students[student_id] = Student(student_name, student_id)

            student = students[student_id]

            if course_name == "Mathematics":
                course = course1
            elif course_name == "Physics":
                course = course2
            else:
                print("Invalid course name.")
                continue

            if course.add_student(student):
                student.enroll_course(course)
                print("Student enrolled successfully.")
            else:
                print("Course is full. Please choose another course.")

        elif option == "2":
            # Display student details
            student_id = input("Enter student ID: ")
            if student_id in students:
                student = students[student_id]
                print(student.get_description())
                for course in student.get_courses():
                    print(f" - {course.get_description()}")
            else:
                print("Student not found.")

        elif option == "3":
            # Display course details
            course_name = input("Enter course name (Mathematics/Physics): ")

            if course_name == "Mathematics":
                print_course_details(course1)
            elif course_name == "Physics":
                print_course_details(course2)
            else:
                print("Invalid course name.")

        elif option == "4":
            # Exit
            break

        else:
            print("Invalid option. Please try again.")
