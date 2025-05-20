# =======================================
# Exercise 05_procedure_functions
# =======================================
# Topic: using stored procedures and functions
# Task: Return the top 10 ProductID and top 10 Customers using Python
# Hint: Use pandas data frames
# =======================================
import pandas as pd
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)

# -- Get top 3 products
# XEC[dbo].[usp_GetTopProductsBySales] 3
sql_query = "EXEC [dbo].[usp_GetTopProductsBySales] ?"

params = 10
df = pd.read_sql(sql_query, conn, params=params)
print(df.tail(5))
# -- Get total spent by customer with ID 29485
# SELECT dbo.ufn_GetTotalSpentByCustomer(29485) AS TotalSpent;
