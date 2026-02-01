import os
import pyodbc
from flask import Flask

app = Flask(_name_)

def get_db_connection():
    # This pulls the secret string we will set in Azure later
    conn_str = os.environ.get('AZURE_SQL_CONNECTION_STRING')
    return pyodbc.connect(conn_str)

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT GETDATE()") # SQL command to get time
        row = cursor.fetchone()
        db_time = row[0]
        return f"<h1>Database Connected! 🚀</h1><p>The current SQL Server time is: {db_time}</p>"
    except Exception as e:
        return f"<h1>Connection Failed ❌</h1><p>Error: {str(e)}</p>"

if _name_ == "_main_":
    app.run()
