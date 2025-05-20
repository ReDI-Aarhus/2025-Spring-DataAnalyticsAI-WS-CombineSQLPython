import pyodbc
from config import db_config 

def get_sql_connection():
    connection_string = (
        f"DRIVER={db_config.driver};"
        f"SERVER={db_config.server};"
        f"DATABASE={db_config.database};"
        f"UID={db_config.username};"
        f"PWD={db_config.password};"
        f"TrustServerCertificate=yes;"
    )
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful.")
        return conn
    except pyodbc.Error as e:
        print("Connection failed:", e)
        return None