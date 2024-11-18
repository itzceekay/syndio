def validate_jobs_payload(employees):
    if not isinstance(employees, list):
        return False, "Invalid input. Expected a list of job data."
    
    if len(employees) == 0:
        return False, "Empty list. Please provide at least one employee."
    
    for employee in employees:
        if not isinstance(employee, dict):
            return False, "Each entry must be a dictionary."
        
        required_keys = ['employee_id', 'department', 'job_title']
        if not all(key in employee for key in required_keys):
            return False, f"Each row must contain {', '.join(required_keys)}."
        
        if not isinstance(employee['employee_id'], int):
            return False, "employee_id must be an integer."
        
        if not isinstance(employee['department'], str) or not isinstance(employee['job_title'], str):
            return False, "department and job_title must be strings."
    
    return True, "Validation successful."