# Importing necessary libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import config.email as eml
import os

# Get password from environment variable
pwd = os.environ['MAIL_USERNAME']
uid = os.environ['MAIL_PASSWORD']

server = "localhost"
db = "AdventureWorks"
port = "5432"
dir = r'DataEngineer/Week_1/Day01'
to = 'davidcaleb@hotmail.com'

# Extract data from sql server
def extract():
    try:
        # Strating directory
        directory = dir
        # Iterate over files in the directory
        for filename in os.listdir(directory):
            # get filename without extension
            file_wo_ext = os.path.splitext(filename)[0]
            # only process excel files
            if filename.endswith(".xlsx"):
                file = os.path.join(directory, filename)
                # checking if it's a file
                if os.path.isfile(file):
                    data = pd.read_excel(file)
                    # call to load
                    load(data, file_wo_ext)
    except Exception as e:
        eml.send_mail(to, "File Upload, Data extract error: ", f"Data extract error: File location {dir}" +str(e))
        print("Data extract error: "+ str(e))

# Load data to postgresql
def load(data, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgrsql://{uid}:{pwd}@{server}:{port}/{db}')
        print(f"Importing rows {rows_imported} to {rows_imported + len(data)}...")

        # Save data to postgresql
        data.to_sql(f"stg_{tbl}", engine, if_exists='replace', index=False)
        rows_imported += len(data)

        # Add elapsed time print out
        print("Data imported successful")
        eml.send_mail(to, "File Uploaded, Data load successful: ", "Data load notification for : " + f"stg_{tbl}")

    except Exception as e:
        eml.send_mail(to, "File Upload Data load error:", f"Data extract error: File location {dir}" + str(e))
        print("Data load error: " + str(e))

try:
    # Call extract function
    data = extract()
except Exception as e:
    eml.send_mail(to, "File Upload, Data extract error: ", f"Function call to file mapping, Data extract error: File location {dir}" + str(e))
    print("Error while extracting data: "+ str(e))