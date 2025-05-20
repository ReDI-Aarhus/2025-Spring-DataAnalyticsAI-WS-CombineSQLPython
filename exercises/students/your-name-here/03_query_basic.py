# =======================================
# Exercise 03_query_basic
# =======================================
# Topic: Basic queries
# Hint: Create a query in database and copy into the dataframe definition.
# =======================================

import pandas as pd
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)
# df = dataframe
sql_query = """
SELECT Name, ProductID FROM SalesLT.Product"""
df = pd.read_sql(sql_query, conn)
print(df.head(25))
