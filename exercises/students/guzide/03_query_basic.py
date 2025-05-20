#=======================================
# Exercise 03_query_basic
#=======================================
# Topic: Basic queries 
# Hint: Create a query in database and copy into the dataframe definition. 
#=======================================
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

import pandas as pd

#df = dataframe
df = pd.read_sql("SELECT * FROM SalesLT.Product ", conn)
print(df.head(25))