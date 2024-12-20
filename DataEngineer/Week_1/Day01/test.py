import pyodbc

driver = "{ODBC Driver 17 for SQL Server}"
server = "localhost\\SQLEXPRESS"
database = "AdventureWorksDW2019"
uid = "etl"
pwd = "demopass"

try:
    conn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}")
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed: " + str(e))
