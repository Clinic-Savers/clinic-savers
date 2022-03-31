from operator import itemgetter
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json

app = Flask(__name__)
CORS(app)

clinic_URL = "http://localhost:5002/clinic"
distance_URL = "http://localhost:5001/checkDist"
appointment_URL = "http://localhost:5003/appointment"
patient_URL = "http://192.168.1.108:5000/patient/"

@app.route("/viewClinics", methods=["POST"])
def viewClinics():
    if request.is_json:
        try:
            patientLocation = request.get_json()
            print("\n Received an patient location in JSON:", patientLocation)

            # 1. Send patientAddress to retrieve clinics sorted by distance
            listOfClinics = retrieveClinics(patientLocation)
            return listOfClinics

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "viewClinics.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def retrieveClinics(patientLocation):
    patientCheck = patientLocation["useHomeAddress"]

    if patientCheck:
        patientNRIC = patientLocation["nric"]

        #invoke patientMS to get the home address 
        print(patient_URL + str(patientNRIC))
        patient_result = invoke_http(patient_URL + str(patientNRIC))
        print(patient_result)
        code = patient_result["code"]
        #cannot find the patient
        if code not in range(200,300):
            return "Patient not logged in"
        else:
            patientPostalCode= str(patient_result["data"]["postalCode"])


    else:
        patientPostalCode = patientLocation["postal"]

    # 2. Invoking clinicMS to get those in the region
    clinic_result = invoke_http(clinic_URL + "/postal/" + patientPostalCode)
    print('\n Clinic result:', clinic_result)

    code = clinic_result["code"]
    #no clinic in the region
    if code not in range(200, 300):
        #get all clinics
        clinic_result = invoke_http(clinic_URL)

        #no clinic in database
        if clinic_result["code"] not in range(200,300):
            return "No Clinic"
    
    listOfClinics = clinic_result["data"]["clinic"]

    final_clinic = {}
    for i in range(0,len(listOfClinics)):
        clinic = listOfClinics[i]

        final_clinic[clinic["clinicId"]] = {
            "name": clinic["clinicName"], 
            "address": clinic["address"],
            "queue": 0
        }

        #3. Invoke appointmentMS to get queue
        appt_url = appointment_URL + str(clinic["clinicId"])
        appointment_result = invoke_http(appt_url)

        code = appointment_result["code"]
        #Got queue 
        if code in range(200, 300):
            queueLength = appointment_result["data"]["queueLength"]
            final_clinic[clinic["clinicId"]]["queue"] = queueLength

    #create object to send to distanceMS
    check_distance = { 
        "patientAddress": patientPostalCode,
        "clinics": [clinic["postalCode"] for clinic in listOfClinics]
    }
    
    #4. Invoke distance microservice
    distance_result = invoke_http(distance_URL, method="POST", json = check_distance)
    print("\n Distance result:", distance_result)

    code = distance_result["code"]
    #location found
    if code in range(200, 300):
        distance_compare = distance_result["data"]["rows"][0]["elements"]

        #append distance
        for i in range(0,len(listOfClinics)):
            final_clinic[listOfClinics[i]["clinicId"]]["distance"] = distance_compare[i]["distance"]["value"]

        #sort by distance
        final_clinic = sorted(final_clinic.values(), key= lambda x: x["distance"])
    else:
        final_clinic = list(final_clinic.values())

    return {
        "code":200,
        "data": final_clinic
    }

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)