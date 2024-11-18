import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from data.db_operations import update_employee_data
from util.validators import validate_jobs_payload

# Load server environment variables
load_dotenv('.env.server')

app = Flask(__name__)

@app.route('/update_employees', methods=['POST'])
def update_employees():
    jobs = request.json
    
    # Validate the payload
    is_valid, message = validate_jobs_payload(jobs)
    if not is_valid:
        return jsonify({"error": message}), 400

    success, message = update_employee_data(jobs)
    
    if success:
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": message}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)