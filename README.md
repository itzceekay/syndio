# Employee Data Update API

This project provides an API endpoint to update employee data in a SQLite database.

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Setup

1. Clone the repository:
```sh
git clone https://github.com/itzceekay/syndio.git

cd syndio
```

2. Create a virtual environment (optional but recommended):

     ```python -m venv venv```

3. Install the required packages:

    ```pip install flask python-dotenv```

4. Set up the environment variables:

    Create a `.env` file in the project root with the following content:
     ```yaml
    PORT=8080
    DATABASE=employees.db
    ```

5. Ensure you have the `employees.db` SQLite database file in the project root directory.


## Running the API

1. From the project root directory, run:

    ```python app/app.py```


2. The API will start running on `http://localhost:8080` (or the port specified in `.env.server`).

## Using the API

To update employee data, send a POST request to the `/update_employees` endpoint with a JSON payload. Example using curl (import the curl in postman):

```bash
curl -X POST -H "Content-Type: application/json" -d '[
{ "employee_id": 1, "department": "Engineering", "job_title": "Senior Engineer" },
{ "employee_id": 2, "department": "Engineering", "job_title": "Super Senior Engineer" },
{ "employee_id": 3, "department": "Sales", "job_title": "Head of Sales"}
]' http://localhost:8080/update_employees
```

## Improvements
1. Use an ORM (Object-Relational Mapping) tool to simplify schema management and provide better control over schema changes.

2. Containerize the project using Docker to ensure consistency across different environments and simplify deployment.