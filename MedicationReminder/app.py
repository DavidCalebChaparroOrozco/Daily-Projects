# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import threading
import time
import json

app = Flask(__name__)

# In-memory storage for patients
patients = []

# Function to send reminders (simulated)
def send_reminder(patient):
    while True:
        now = datetime.now().strftime("%H:%M")
        for med_time in patient['medication_times']:
            if now == med_time:
                print(f"Reminder: Time to give {patient['name']} their medication!")
                # Wait a minute before checking again
                time.sleep(60)  

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', patients=patients)

# Route to add a new patient
@app.route('/add_patient', methods=['POST'])
def add_patient():
    # Get patient data from the form
    patient_id = request.form['id']
    name = request.form['name']
    room_number = request.form['room_number']
    medications = request.form['medications'].split(',')
    allergies = request.form.get('allergies') == 'on'
    allergy_details = request.form.get('allergy_details', '')
    falls = request.form.get('falls') == 'on'
    description = request.form['description']
    
    # Get medication times from the form and split them by medication
    medication_times = request.form.getlist('medication_times[]')
    
    # Create a patient dictionary and add it to the list
    patient = {
        'id': patient_id,
        'name': name,
        'room_number': room_number,
        'medications': medications,
        'allergies': allergies,
        'allergy_details': allergy_details,
        'falls': falls,
        'description': description,
        'medication_times': [time.strip() for time in medication_times if time.strip()]
    }
    
    patients.append(patient)

    # Start a reminder thread for this patient
    threading.Thread(target=send_reminder, args=(patient,), daemon=True).start()

    return redirect(url_for('index'))

# Route to delete a patient
@app.route('/delete_patient/<int:index>', methods=['POST'])
def delete_patient(index):
    if 0 <= index < len(patients):
        del patients[index]
    return redirect(url_for('index'))

# Route to edit a patient's information
@app.route('/edit_patient/<int:index>', methods=['POST'])
def edit_patient(index):
    if 0 <= index < len(patients):
        patient = patients[index]
        patient['name'] = request.form['name']
        patient['room_number'] = request.form['room_number']
        patient['medications'] = request.form['medications'].split(',')
        patient['allergies'] = request.form.get('allergies') == 'on'
        patient['allergy_details'] = request.form.get('allergy_details', '')
        patient['falls'] = request.form.get('falls') == 'on'
        patient['description'] = request.form['description']
        
        # Update medication times from the form
        medication_times = request.form.getlist('medication_times[]')
        patient['medication_times'] = [time.strip() for time in medication_times if time.strip()]
    
    return redirect(url_for('index'))

# Route to generate weekly report in JSON format
@app.route('/generate_report', methods=['GET'])
def generate_report():
    with open('weekly_report.json', 'w') as json_file:
        json.dump(patients, json_file)
    return jsonify({"message": "Report generated successfully!"})

# Route to clear all patients
@app.route('/clear_patients', methods=['POST'])
def clear_patients():
    patients.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)