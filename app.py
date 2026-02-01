import os
import pyodbc
from flask import Flask

app = Flask(_name_)

def get_db_connection():
    
    conn_str = os.environ.get('AZURE_SQL_CONNECTION_STRING')
    
    if 'DRIVER' not in conn_str:
        driver = '{ODBC Driver 17 for SQL Server}'
        conn_str = f"DRIVER={driver};{conn_str}"
    
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
        
        return f"<h1>Connection Failed ❌</h1><p>Error: {str(e)}</p>"
