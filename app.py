import os
import pyodbc
from flask import Flask

app = Flask(_name_)

def get_db_connection():
    # 1. Get the secret string you added in Azure Portal
    conn_str = os.environ.get('AZURE_SQL_CONNECTION_STRING')
    
    # 2. Add the Driver name (Required for Linux)
    # Most Azure Linux plans now use Driver 18
    if 'DRIVER' not in conn_str:
        driver = '{ODBC Driver 18 for SQL Server}'
        conn_str = f"DRIVER={driver};{conn_str}"
    
    # 3. Add TrustServerCertificate for Azure SQL (Prevents SSL errors)
    if 'TrustServerCertificate' not in conn_str:
        conn_str += ";TrustServerCertificate=yes;"
        
    return pyodbc.connect(conn_str)

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT GETDATE()") 
        row = cursor.fetchone()
        db_time = row[0]
        conn.close()
        return f"<h1>Database Connected! 🚀</h1><p>SQL Server Time: {db_time}</p>"
    except Exception as e:
        # This will show you exactly what is failing on the webpage!
        return f"<h1>Connection Failed ❌</h1><p>Error: {str(e)}</p>"
