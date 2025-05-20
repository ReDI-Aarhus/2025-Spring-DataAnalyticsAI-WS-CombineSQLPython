from utils.db_utils import get_sql_connection

conn = get_sql_connection()

sql_query = """
    SELECT TOP 5 * FROM SalesLT.Customer
"""

if conn:
    cursor = conn.cursor()
    cursor.execute(sql_query)
    for row in cursor.fetchall():
        print(row)
    conn.close()
