from controller.controller import CatController
from model.model import CatModel
from view.view import CatView

def main():
    model = CatModel()
    view = CatView()
    controller = CatController(model, view)

    while True:
        view.display_menu()
        choice = view.get_input("Enter your choice: ", lambda x: x.isdigit() and 1 <= int(x) <= 10)
        choice = int(choice)
        
        if choice == 1:
            controller.view_all_cats()
        elif choice == 2:
            name = view.get_input("Enter cat's name: ")
            breed = view.get_input("Enter cat's breed: ")
            age = int(view.get_input("Enter cat's age: ", lambda x: x.isdigit() and int(x) > 0))
            controller.add_cat(name, breed, age)
        elif choice == 3:
            name = view.get_input("Enter the name of the cat to remove: ")
            controller.remove_cat(name)
        elif choice == 4:
            breed = view.get_input("Enter the breed to search: ")
            controller.search_by_breed(breed)
        elif choice == 5:
            name = view.get_input("Enter the cat's name: ")
            new_age = int(view.get_input("Enter new age: ", lambda x: x.isdigit() and int(x) > 0))
            controller.update_cat_age(name, new_age)
        elif choice == 6:
            controller.show_statistics()
        elif choice == 7:
            controller.save_to_file()
        elif choice == 8:
            controller.load_from_file()
        elif choice == 9:
            controller.visualize_data()
        elif choice == 10:
            print("Exiting... Goodbye!")
            break

if __name__ == "__main__":
    main()