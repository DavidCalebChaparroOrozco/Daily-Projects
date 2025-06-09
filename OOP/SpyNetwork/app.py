from model.model import SpyModel
from view.view import SpyView
from controller.controller import SpyController

def main():
    try:
        # Initialize MVC components
        model = SpyModel()
        view = SpyView()
        controller = SpyController(model, view)
        
        # Start the application
        controller.run()
    except KeyboardInterrupt:
        print("\nOperation aborted by user.")
    except Exception as e:
        print(f"\nA critical error occurred: {str(e)}")

if __name__ == "__main__":
    main()