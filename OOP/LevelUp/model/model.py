class JobModel:
    def __init__(self, job_id, title, company, salary, experience_required, description, benefits, schedule, remote):
        self.job_id = job_id
        self.title = title
        self.company = company
        self.salary = salary
        self.experience_required = experience_required
        self.description = description
        self.benefits = benefits
        self.schedule = schedule
        self.remote = remote

    def __str__(self):
        remote_status = "Remote" if self.remote else "On-site"
        return (f"Job ID: {self.job_id}, Title: {self.title}, Company: {self.company}, Salary: {self.salary}, "
                f"Experience Required: {self.experience_required} years, Description: {self.description}, "
                f"Benefits: {self.benefits}, Schedule: {self.schedule}, Work Mode: {remote_status}")
