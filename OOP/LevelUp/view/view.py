import re

class JobsView:
    @staticmethod
    def display_menu():
        print("\nWelcome to the Level Up Jobs")
        print("1. View all job offers")
        print("2. Add new job offer")
        print("3. Edit job offer")
        print("4. Remove job offer")
        print("5. Exit")
        print("=".center(50, "="))

    @staticmethod
    def display_job_offer(job_offer):
        if not job_offer:
            print("There are no job offers available.")
        else:
            for job in job_offer:
                print(job)

    @staticmethod
    def get_job_details():
        title = input("Enter job Title: ")
        company = input("Enter Company: ")
        salary = JobsView.validate_salary()
        experience_required = JobsView.validate_experience()
        description = input("Enter job description: ")
        benefits = input("Enter benefits: ")
        schedule = input("Enter work schedule: ")
        remote = JobsView.validate_remote_option()

        return title, company, salary, experience_required, description, benefits, schedule, remote

    @staticmethod
    def get_user_details():
        name = JobsView.validate_name()
        email = JobsView.validate_email()
        phone = JobsView.validate_phone()
        technology = input("Enter technology (programming languages): ")
        experience = JobsView.validate_experience()
        other_info = input("Enter other info (optional): ")

        return name, email, phone, technology, experience, other_info

    @staticmethod
    def validate_name():
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                return name
            else:
                print("Error: Name cannot contain numbers or special characters. Please try again.")

    @staticmethod
    def validate_email():
        while True:
            email = input("Enter your email: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Error: Invalid email format. Please try again.")

    @staticmethod
    def validate_phone():
        while True:
            phone = input("Enter your phone number: ")
            if phone.isdigit() and len(phone) == 10:
                return phone
            else:
                print("Error: Phone number must contain 10 digits. Please try again.")

    @staticmethod
    def validate_salary():
        while True:
            try:
                salary = float(input("Enter Salary: "))
                return salary
            except ValueError:
                print("Error: Salary must be a valid number. Please try again.")

    @staticmethod
    def validate_experience():
        while True:
            try:
                experience = int(input("Enter years of experience: "))
                return experience
            except ValueError:
                print("Error: Experience must be a valid number. Please try again.")

    @staticmethod
    def validate_remote_option():
        while True:
            option = input("Is this job remote? (y/n): ").lower()
            if option in ['y', 'n']:
                return True if option == 'y' else False
            else:
                print("Error: Please enter 'y' for Yes or 'n' for No.")

    @staticmethod
    def display_success_message(message):
        print(f"Success: {message}")

    @staticmethod
    def display_error_message(message):
        print(f"Error: {message}")

    @staticmethod
    def get_job_id():
        return input("Enter the job ID to remove: ")