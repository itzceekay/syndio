import sqlite3
from data.db_queries import get_db_connection, check_and_modify_employees_table

def update_employee_data(jobs):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check and modify the employees table if necessary
        check_and_modify_employees_table(cursor)

        for job in jobs:
            # Update the employees table with department and job_title
            cursor.execute('''UPDATE employees 
                              SET department = ?, job_title = ? 
                              WHERE id = ?''',
                           (job['department'], job['job_title'], job['employee_id']))
            
            # If no rows were updated, the employee doesn't exist
            if cursor.rowcount == 0:
                conn.rollback()
                return False, f"Employee with id {job['employee_id']} does not exist"

        conn.commit()
        return True, "Employee data updated successfully"
    except sqlite3.Error as e:
        conn.rollback()
        return False, f"Database error: {str(e)}"
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        conn.close()