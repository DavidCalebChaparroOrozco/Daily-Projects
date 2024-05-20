# Import necessary libraries
import csv
import requests
from bs4 import BeautifulSoup

# URL of the Python jobs page
URL = "https://www.python.org/jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Find the main job container
job_container = soup.find("ol", class_="list-recent-jobs")

# Find all job listings within the container
job_elements = job_container.find_all("li") if job_container else []

# Open a CSV file for writing
with open("python_jobs.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Job Title", "Company", "Location", "Posted Date", "Job Types"])
    
    for job_element in job_elements:
        # Find the job title
        title_element = job_element.find("a")
        title = title_element.text.strip() if title_element else "N/A"
        
        # Find the company
        company_element = job_element.find("span", class_="listing-company-name")
        if company_element:
            company_lines = company_element.stripped_strings
            company = list(company_lines)[-1].strip()
        else:
            company = "N/A"
        
        # Find the location
        location_element = job_element.find("span", class_="listing-location")
        location = location_element.get_text(strip=True) if location_element else "N/A"
        
        # Find the posting date
        posted_element = job_element.find("time")
        posted_date = posted_element.text.strip() if posted_element else "N/A"
        
        # Find the job types (if any)
        job_type_elements = job_element.find_all("span", class_="listing-job-type")
        job_types = ", ".join([job_type.text.strip() for job_type in job_type_elements]) if job_type_elements else "N/A"
        
        # Write the job details to the CSV file
        writer.writerow([title, company, location, posted_date, job_types])

print("Job data has been written to python_jobs.csv")
