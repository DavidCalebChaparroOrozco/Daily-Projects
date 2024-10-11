# main.py - Entry point of the cellphone inventory system.

from controller.controller import Controller

if __name__ == "__main__":
    # Create a Controller object and run the program
    controller = Controller()
    controller.run()
