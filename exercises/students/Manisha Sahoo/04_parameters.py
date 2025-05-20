#=======================================
# Exercise 04_parameters
#=======================================
# Topic: Parameters
# Task: Create a parameterized query filtering by any column. 
# Hint: Create a query in database and copy into the sql_query variable
#=======================================

sql_query = "SELECT * FROM users WHERE country = ?"
params = ("Germany",)
df = pd.read_sql(sql_query, conn, params=params)

print(df.head(25))