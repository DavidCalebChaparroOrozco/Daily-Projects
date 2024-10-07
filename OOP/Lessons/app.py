from view.view import View
from controller.controller import Controller

if __name__ == "__main__":
    view = View()
    controller = Controller(view)

    while True:
        option = view.display_menu()
        
        if option == "1":
            controller.subscribe_student_to_lesson()
        elif option == "2":
            controller.display_student_details()
        elif option == "3":
            controller.display_lesson_details()
        elif option == "4":
            controller.check_instructor_for_lesson()
        elif option == "5":
            break
        else:
            view.display_message("Invalid option. Please try again.")
