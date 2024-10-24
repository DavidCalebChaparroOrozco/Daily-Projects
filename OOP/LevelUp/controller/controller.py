from model.model import JobModel
from view.view import JobsView

class JobsController:
    def __init__(self):
        self.jobs = []
        self.next_job_id = 1

    def add_job(self):
        # Get job details from the view
        title, company, salary, experience_required, description, benefits, schedule, remote = JobsView.get_job_details()
        
        # Automatically assign a unique ID to the new job
        job_id = self.next_job_id
        self.next_job_id += 1  
        
        # Create a new job with the ID and details
        new_job = JobModel(job_id, title, company, salary, experience_required, description, benefits, schedule, remote)
        self.jobs.append(new_job)
        
        JobsView.display_success_message(f"Job '{title}' added successfully with ID {job_id}!")

    def view_jobs(self):
        JobsView.display_job_offer(self.jobs)

    def edit_job(self):
        job_id = JobsView.get_job_id()
        for job in self.jobs:
            if str(job.job_id) == job_id: 

                JobsView.display_success_message(f"Editing job ID '{job_id}'")
                title, company, salary, experience_required, description, benefits, schedule, remote = JobsView.get_job_details()
                
                job.title = title
                job.company = company
                job.salary = salary
                job.experience_required = experience_required
                job.description = description
                job.benefits = benefits
                job.schedule = schedule
                job.remote = remote
                
                JobsView.display_success_message(f"Job ID '{job_id}' updated successfully!")
                return
        JobsView.display_error_message(f"Job ID '{job_id}' not found.")

    def remove_job(self):
        job_id = JobsView.get_job_id() 
        for job in self.jobs:
            if str(job.job_id) == job_id:
                self.jobs.remove(job)
                JobsView.display_success_message(f"Job ID '{job_id}' removed successfully!")
                return
        JobsView.display_error_message(f"Job ID '{job_id}' not found.")

    def run(self):
        while True:
            JobsView.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_jobs()
            elif choice == '2':
                self.add_job()
            elif choice == '3':
                self.edit_job()
            elif choice == '4':
                self.remove_job()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
