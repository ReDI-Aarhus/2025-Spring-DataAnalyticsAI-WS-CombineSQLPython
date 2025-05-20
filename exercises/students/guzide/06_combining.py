#=======================================
# Exercise 06_combining
#=======================================
# Topic: using stored procedures and functions
# Task: Return the top 10 ProductID and top 10 Customers using Python 
# Hint: Use pandas data frames
#=======================================
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)
import pandas as pd

# Call stored procedure
df = pd.read_sql("EXEC dbo.usp_GetTopProductsBySales @TopX = 10", conn)

# Define category logic
def classify_sales(sales):
    if sales >= 35000:
        return "Gold"
    elif sales >= 20000:
        return "Silver"
    elif sales >= 10000:
        return "Platin"
    else:
        return "Bronze"

# Add category
df["Category"] = df["TotalSales"].apply(classify_sales)

print(df)