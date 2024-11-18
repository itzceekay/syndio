import os
import sqlite3
from dotenv import load_dotenv

# Load database environment variables
load_dotenv('.env.db')

DATABASE = os.getenv('DATABASE', 'employees.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def check_and_modify_employees_table(cursor):
    # Check if the employees table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employees'")
    if cursor.fetchone() is None:
        raise Exception("Employees table does not exist")

    # Get the current schema of the employees table
    cursor.execute("PRAGMA table_info(employees)")
    columns = {row[1]: row[2] for row in cursor.fetchall()}

    # Check if the required columns exist, add them if they don't
    if 'department' not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN department TEXT")
    
    if 'job_title' not in columns:
        cursor.execute("ALTER TABLE employees ADD COLUMN job_title TEXT")