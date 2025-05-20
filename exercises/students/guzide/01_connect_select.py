#=======================================
# Exercise 01_connect_select
#=======================================
# Topic: connect & SELECT basics

#=======================================

#Run in terminal: pip install pyodbc pandas
import pyodbc

SERVER = 'redi-sandbox-01-sql.database.windows.net'
DATABASE = 'ReDI-SQL-Fundamentals-01'
USERNAME = 'Student01'
PASSWORD = 'StrongPassword!123'
connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = """
    SELECT 
        1 AS Number,
        'Jane Doe' AS StudentName 

        UNION ALL
    
    SELECT
        2 AS Number,
        'John Doe' AS StudentName
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()

#print total resultset 
print("print(records):") 
print(records) 

#Divider
print("\n" + "-" * 50 + "\n")

#print total resultset - formatted

#print header
print(f"Number\t""StudentName")
for r in records:
    #print records
    print(f"{r.Number}\t{r.StudentName}")
    
