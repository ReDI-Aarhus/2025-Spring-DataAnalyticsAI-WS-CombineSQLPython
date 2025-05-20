# =======================================
# Exercise 04_parameters
# =======================================
# Topic: Parameters
# Task: Create a parameterized query filtering by any column.
# Hint: Create a query in database and copy into the sql_query variable
# =======================================
import pandas as pd
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)
sql_query = "SELECT * FROM SalesLT.product WHERE color = ?"
params = ("Black",)
df = pd.read_sql(sql_query, conn, params=params)

print(df.head(25))
