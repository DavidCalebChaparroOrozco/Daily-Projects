# Importing necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import os

# Get password from environment var
# pwd = os.environ['PGPASS']
# uid = os.environ['PGUID']

pwd = "demopass"
uid = "etl"

# Sql db details
driver = "{ODBC Driver 17 for SQL Server}"
server = "localhost\\SQLEXPRESS,1433"  
database = "AdventureWorksDW2019;"

# Extract data from sql server
def extract():
    try:
        connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        src_engine = create_engine(connection_url)
        src_conn = src_engine.connect()
        # Execute query
        query = """ select  t.name as table_name
        from sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductSubcategory','DimProductCategory','DimSalesTerritory','FactInternetSales') """
        src_tables = pd.read_sql_query(query, src_conn).to_dict()['table_name']

        for id in src_tables:
            table_name = src_tables[id]
            data = pd.read_sql_query(f'select * FROM {table_name}', src_conn)
            load(data, table_name)

    except Exception as e:
        print("Data extract error: " + str(e))

# Load data to postgres
def load(data, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/adventureworks')
        print(f'importing rows {rows_imported} to {rows_imported + len(data)}... for table {tbl}')
        # Save data to postgres
        data.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, chunksize=100000)
        rows_imported += len(data)
        # Add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    # Call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))