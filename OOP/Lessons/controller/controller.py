from model.person import Student, Instructor
from model.lesson import Lesson

class Controller:
    def __init__(self, view):
        self.view = view
        self.students = {}
        self.instructors = {}

    def subscribe_student_to_lesson(self):
        try:
            student_name, student_id = self.view.get_student_details()
            if student_id not in self.students:
                self.students[student_id] = Student(student_name, student_id)
            student = self.students[student_id]

            lesson_topic = self.view.get_lesson_topic()

            instructor_name, instructor_id = self.view.get_instructor_details()
            if instructor_id not in self.instructors:
                self.instructors[instructor_id] = Instructor(instructor_name, instructor_id)
            instructor = self.instructors[instructor_id]

            lesson = Lesson(lesson_topic, lesson_topic, instructor, 2)  # Example duration
            student.subscribe_to_lesson(lesson)
            instructor.add_lesson(lesson)

            self.view.display_message("Subscription successful.")
        except ValueError as e:
            self.view.display_message(str(e))

    def display_student_details(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            self.view.display_student_subscriptions(student)
        else:
            self.view.display_message("Student not found.")

    def display_lesson_details(self):
        lesson_title = self.view.get_lesson_title()
        instructor_name = self.view.get_instructor_details()[0]
        lesson = Lesson(lesson_title, "AI", instructor_name, 3)
        self.view.display_lesson_details(lesson)

    def check_instructor_for_lesson(self):
        lesson_topic = self.view.get_lesson_topic()
        instructor_found = None
        for instructor in self.instructors.values():
            lesson = instructor.teaches_lesson(lesson_topic)
            if lesson:
                instructor_found = instructor
                break

        if instructor_found:
            self.view.display_instructor_for_lesson(instructor_found)
        else:
            self.view.display_message(f"No instructor found for the lesson topic '{lesson_topic}'")