#=======================================
# Exercise 06_combining
#=======================================
# Topic: using stored procedures and functions
# Task: Return the top 10 ProductID and top 10 Customers using Python 
# Hint: Use pandas data frames
#=======================================


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