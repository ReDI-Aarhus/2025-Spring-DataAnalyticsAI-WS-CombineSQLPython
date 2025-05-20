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

