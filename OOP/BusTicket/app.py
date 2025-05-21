from controller.controller import BusTicketController

# Main function to initialize and run the Bus Ticket Simulator application.
def main():
    try:
        # Initialize the controller
        app = BusTicketController()
        
        # Start the application
        app.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()