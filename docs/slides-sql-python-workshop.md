---
marp: true
theme: default
paginate: true
---

<style>
section {
    font-family: 'Open Sans', sans-serif;
    background-color: hsla(195, 50%, 96.86%, 1);
    color: #003b4a; /* A deep teal for contrast */
    font-family: 'Segoe UI', sans-serif;
    font-size: 2em;
    padding: 30px;
}
h1, h2, h3 {
   color: #0056b3;
 }
 ul {
   list-style-type: square;
   padding-left: 1.5em;
 }
 
 li {
   font-size: 22px;
   line-height: 1.5;
   margin-bottom: 0.3em;
 }
 
 li::marker {
   color: #0056b3;
 }
</style>

# Combining SQL & Python Workshop

🗓 **Date:** 2025-05-20 (May 20th, 2025) <br/> 
🕠 **Time:** 17:30–20:00  
💻 **Tools:** VS Code, Azure SQL DB, GitHub

---
## 📅 Agenda (17:30–20:00)

1. **Introduction & Setup** (17:30–18:00)  
2. **SQL vs Python: Strengths & Use Cases** (18:00–18:15)  
3. **Connecting Python to SQL** (18:15–18:30)  
4. **Querying Data: Tables, Views, Parameters** (18:30–18:50)  
5. **Calling Stored Procedures & Functions** (18:50–19:10)  
6. **Combining Python Logic + SQL Power** (19:10–19:30)  
7. **Challenge: Insert & Query App** (19:30–19:50)  
8. **Wrap-Up & What’s Next** (19:50–20:00)

---

## 🛠 1. Git & SQL Workflow

* Create branch per exercise.
* Work in `exercise/students/your-name-here/0x_xyz.py` files
* Use `git add`, `commit`, `push`


---

## 🛠 1. GitHub & Version Control Process - First exercise
Read: [git-cheatsheet.md](git-cheatsheet.md) in repos
###### Main steps:
* Clone the repo and create your exercise branch.
* Rename `/<your-name-here>/` folder.
* Work on exercise in dedicated .sql file: [01_connect_select.py](../exercises/students/your-name-here/01_connect_select.py)
* Add changes using `git add`, commit with `git commit -m`, and push with `git push --set-upstream`.

```bash
# create branch
git checkout -b "jane/01_connect_select"
# make your changes
git add .
git commit -m "Completed 01_connect_select exercise"
git push --set-upstream origin "jane/01_connect_select"
```
---
## 🛠 1. GitHub & Version Control Process - following exercises
Read: [git-cheatsheet.md](git-cheatsheet.md) in repos
###### Main steps:
* Create your exercise branch.
* Work on exercise in dedicated .sql file: [03_query_basic.py](../exercises/students/your-name-here/03_query_basic.py) 
* Add changes using `git add`, commit with `git commit -m`, and push with `git push --set-upstream`.

```bash
# create branch
git checkout -b "03_query_basic"
# make your changes
git add .
git commit -m "Completed 03_query_basic exercise"
git push --set-upstream origin "jane/03_query_basic"
```
* Repeat for [04_parameters.py](../exercises/students/your-name-here/04_parameters.py) & [05_procedure_functions.py](../exercises/students/your-name-here/05_procedure_functions.py)

---

## 🛠 1. Setup Instructions

```
pip install pyodbc pandas
```

Connection examples:

```python
# SQL Server (pyodbc)
import pyodbc
conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=testdb;UID=sa;PWD=your_password")
```
<br>

✅ **Exercise: [01_connect_select.py](../exercises/students/your-name-here/01_connect_select.py)** 
- path: exercises\students\your-name-here\01_connect_select.py

---

## ⚖ 2. SQL vs Python – When to Use What?

### It depends :smile:

| Use Case | SQL | Python |
|:----------|:-----:|:--------:|
| Filtering, Joining, Aggregation | ✅ Best | 👎 |
| Complex Data Cleaning & Transformation | 👎 | ✅ Best |
| Business Rules | ✅ Stored Procedures | ✅ Flexible Logic |
| Reporting Views | ✅ | 👎 |
| Visualizations & ML | 👎 | ✅ |

---

## ⚖ 2. SQL vs Python – When to Use What?

### My overall preference: 
- Python for orchestration
- Python running generalized functions
  - **Aim for reusable code and patterns!**
- Pyhton call objects: stored procedure, function, tables, views
- Prepare "output" in SQL
- Handle joins, filters, queries, naming etc. in SQL

We want to avoid that you have to recompile an app every time you need to make small changes. 

---

## 🔌 3. Connecting & Querying with Python

_Using pandas dataframes_
### Basic Query Example:

```python
import pandas as pd

#df = dataframe
df = pd.read_sql("SELECT * FROM ...", conn)
print(df.head(25))

```
✅ **Exercise: [03_query_basic.py](../exercises/students/your-name-here/03_query_basic.py)**  
Write a Python script that:
- Connects to your DB
- Reads from a `products` or `customers` table
- Loads it into a pandas DataFrame
---


## 🗂 4. Tables, Views & Parameterized Queries
### SQL View
```sql
CREATE VIEW [SalesLT].[vGetAllCategories]
AS
-- Returns the Parent-Child hierarchy of product categories.
WITH CategoryCTE([ParentProductCategoryID], [ProductCategoryID], [Name]) AS
(
    --Anchor: Find the categories with no parents (i.e. highest level)
    SELECT [ParentProductCategoryID], [ProductCategoryID], [Name]
    FROM SalesLT.ProductCategory
    WHERE ParentProductCategoryID IS NULL

UNION ALL

    --Union the children to each parent.
    SELECT C.[ParentProductCategoryID], C.[ProductCategoryID], C.[Name]
    FROM SalesLT.ProductCategory AS C
    INNER JOIN CategoryCTE AS BC ON BC.ProductCategoryID = C.ParentProductCategoryID
)
--join back to categories to implicitly filter out the anchor
SELECT PC.[Name] AS [ParentProductCategoryName], CCTE.[Name] as [ProductCategoryName], CCTE.[ProductCategoryID]
FROM CategoryCTE AS CCTE
JOIN SalesLT.ProductCategory AS PC
ON PC.[ProductCategoryID] = CCTE.[ParentProductCategoryID]
```

---
## 🗂 4. Tables, Views & Parameterized Queries

### Python script:
```python
df = pd.read_sql("SELECT * FROM [SalesLT].[vGetAllCategories]", conn)
```
---

## 🗂 4. Tables, Views & Parameterized Queries

### Parameterized Query:
```python
sql_query = "SELECT * FROM users WHERE country = ?"
params = ("Germany",)
df = pd.read_sql(sql_query, conn, params=params)
```
✅ **Exercise: [04_parameters.py](../exercises/students/your-name-here/04_parameters.py)**  
- Create a parameterized query filtering by any column
- Try both correct and incorrect inputs (e.g., wrong data type)

---
## 🧠 5. Stored Procedures & Functions
### Stored Procedure:
```sql
CREATE PROCEDURE usp_GetTopProductsBySales
    @TopX INT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT TOP (@TopX)
        p.ProductID,
        p.Name AS ProductName,
        SUM(s.LineTotal) AS TotalSales
    FROM
        SalesLT.SalesOrderDetail s
    INNER JOIN
        SalesLT.Product p ON s.ProductID = p.ProductID
    GROUP BY
        p.ProductID, p.Name
    ORDER BY
        TotalSales DESC;
END;
```


---

## 🧠 5. Stored Procedures & Functions
### Function:
```sql
CREATE FUNCTION ufn_GetTotalSpentByCustomer
(
    @CustomerID INT
)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalSpent MONEY;

    SELECT @TotalSpent = SUM(s.LineTotal)
    FROM SalesLT.SalesOrderHeader h
    INNER JOIN SalesLT.SalesOrderDetail s ON h.SalesOrderID = s.SalesOrderID
    WHERE h.CustomerID = @CustomerID;

    RETURN ISNULL(@TotalSpent, 0);
END;
```


---

## 🧠 5. Stored Procedures & Functions

### Calling Stored Procedure (SQL Server):
##### T-SQL
```sql
EXEC usp_GetTopProductsBySales @TopX = 5;
```
##### Python
```python
cursor.execute("EXEC usp_GetTopProductsBySales ?", (5))
```
### Scalar Function (SQL Server):
```sql
-- Get total spent by customer with ID 29485
SELECT dbo.ufn_GetTotalSpentByCustomer(29485) AS TotalSpent;

SELECT 
    c.CustomerID, c.FirstName, c.LastName,
    dbo.ufn_GetTotalSpentByCustomer(c.CustomerID) AS TotalSpent
FROM SalesLT.Customer c
ORDER BY TotalSpent DESC;
```

---

## 🧠 5. Stored Procedures & Functions

✅ **Exercise [05__procedure_functions.py](../exercises/students/your-name-here/05_procedure_functions.py):**
- Call a stored procedure & function:
```sql
EXEC usp_GetTopProductsBySales

SELECT dbo.ufn_GetTotalSpentByCustomer
```

Then call it from Python and print the result.

---

## 🤝 6. Combining Logic – Python + SQL

Use SQL for the heavy lifting, Python for business logic:

```python
# Call stored procedure
df = pd.read_sql("EXEC dbo.usp_GetTopProductsBySales @TopX = 10", conn)

# Define category logic
def classify_sales(sales):
    if sales >= 35000:
        return "Gold"
    elif sales >= 20000:
        return "Silver"
    else:
        return "Bronze"

# Add category
df["Category"] = df["TotalSales"].apply(classify_sales)

print(df)
```

✅ **Exercise: [06_combining.py](../exercises/students/your-name-here/06_combining.py)**  
- try the script and try adjust it.

---

## 🧪 7. Challenge: Insert & Query Mini App

### Goal:
- Get the app functions configured
- We will try to export data from SQL results into .csv
- We will try to read it back and transform data
- Optional: basic user input

```python
data = {'Country': ['Belgium',  'India',  'Brazil'],

'Capital': ['Brussels',  'New Delhi',  'Brasilia'],

'Population': [11190846, 1303171035, 207847528]} 

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

df.to_csv('myDataFrame.csv')
pd.read_csv('myDataFrame.csv', header=None, nrows=5)


```


---
## 8. Wrap-Up & What’s Next

### What You’ve Learned:
- How Python connects to a SQL database
- When to use SQL, Python, or both
- Reading, filtering, and transforming data
- Calling procedures & inserting records

### Additional Resources

* Azure SQL sample databases: [MS Docs](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms)
* Practice site: [sqlpad.io](https://sqlpad.io/)

