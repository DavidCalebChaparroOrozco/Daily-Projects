# Import necessary libraries
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate employee data

# 50 employees
employee_ids = [f"E{str(i).zfill(3)}" for i in range(1, 51)]  
departments_roles = {
    "Sales": ["Sales Representative", "Sales Manager"],
    "IT": ["Developer", "System Administrator"],
    "HR": ["HR Specialist", "Recruiter"],
    "Finance": ["Accountant", "Financial Analyst"],
    "Operations": ["Coordinator", "Operations Manager"]
}

# Generate date range for 3 months (approx. 60 working days excluding weekends)
start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 8, 31)
# Business days only
date_range = pd.date_range(start=start_date, end=end_date, freq='B')  

# Generate dataset
records = []
for date in date_range:
    for emp_id in employee_ids:
        dept = random.choice(list(departments_roles.keys()))
        role = random.choice(departments_roles[dept])
        
        # Randomly decide if employee is absent (5% chance)
        if random.random() < 0.05:
            continue

        # Entry and exit time generation with randomness and possible lateness
        entry_hour = random.choices([8, 9, 10], weights=[0.2, 0.7, 0.1])[0]
        entry_minute = random.choice([0, 5, 10, 15, 30])
        entry_time = datetime(date.year, date.month, date.day, entry_hour, entry_minute)

        work_hours = random.randint(7, 9)
        exit_time = entry_time + timedelta(hours=work_hours, minutes=random.choice([0, 15, 30]))

        records.append({
            "EmployeeID": emp_id,
            "Date": date.strftime("%Y-%m-%d"),
            "EntryTime": entry_time.strftime("%H:%M"),
            "ExitTime": exit_time.strftime("%H:%M"),
            "Department": dept,
            "Role": role
        })

# Create DataFrame
data = pd.DataFrame(records)

# Save dataset to CSV
file_path = "employee_attendance_log.csv"
data.to_csv(file_path, index=False)

print(f"Sample employee attendance data generated and saved to {file_path}")
file_path