#=======================================
# Exercise 05_procedure_functions
#=======================================
# Topic: using stored procedures and functions
# Task: Return the top 10 ProductID and top 10 Customers using Python 
# Hint: Use pandas data frames
#=======================================

# -- Get top 3 products
# EXEC [dbo].[usp_GetTopProductsBySales] 3
# -- Get total spent by customer with ID 29485
# SELECT dbo.ufn_GetTotalSpentByCustomer(29485) AS TotalSpent;
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

import pandas as pd
sql_query = """
    EXEC [dbo].[usp_GetTopProductsBySales] ?
"""
params = (5)
df = pd.read_sql(sql_query, conn, params=params)

print(df.head(100))

sql_query2 = """
    SELECT dbo.ufn_GetTotalSpentByCustomer(?) AS TotalSpent
"""
params = (29485)
df = pd.read_sql(sql_query2, conn, params=params)
print(df.head(100))