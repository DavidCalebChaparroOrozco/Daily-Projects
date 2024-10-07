class View:
    def display_menu(self):
        print("\nLesson Subscription System")
        print("1. Subscribe to a lesson topic")
        print("2. Display student details")
        print("3. Display lesson details")
        print("4. Check which instructor is teaching a lesson")
        print("5. Exit")
        print("=" * 50)
        return input("Select an option: ")

    def get_student_details(self):
        student_name = input("Enter student name (letters only): ")
        student_id = input("Enter student ID: ")
        return student_name, student_id

    def get_instructor_details(self):
        instructor_name = input("Enter instructor name (letters only): ")
        instructor_id = input("Enter instructor ID: ")
        return instructor_name, instructor_id

    def get_lesson_topic(self):
        return input("Enter lesson topic (e.g., Web Development, AI, Mobile Development): ")

    def get_lesson_title(self):
        return input("Enter lesson title: ")

    def get_lesson_duration(self):
        return input("Enter lesson duration (in hours): ")

    def display_message(self, message):
        print(message)

    def display_student_subscriptions(self, student):
        print(student.get_description())
        for lesson in student.get_subscriptions():
            print(f" - Subscribed to: {lesson.get_topic()}")

    def display_lesson_details(self, lesson):
        print(lesson.get_description())

    def display_instructor_for_lesson(self, instructor):
        print(f"Instructor {instructor.get_name()} is teaching the lesson.")
