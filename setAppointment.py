from operator import itemgetter
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import json

app = Flask(__name__)
CORS(app)

appt_timing_URL = environ.get('appt_URL') or "http://localhost:5003/appointment"
appt_URL = environ.get('appt_URL') or "http://localhost:5003/set_appointment"
patient_URL = environ.get('patient_URL') or "http://192.168.1.108:5000/patient/"
subsidy_URL = environ.get('subsidy_URL') or "http://localhost:5004/subsidy/"

@app.route("/set_timing", methods=["POST"])
def set_timing():
    if request.is_json:
        try:
            appt_date = request.get_json()
            print("\n Appointment date  and clinic ID in JSON:", appt_date)

            #1. Send appt details to set appointment
            appt_result = check_timing(appt_date)
            return appt_result

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "setAppointment.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

def check_timing(appt_date):
    clinicId = appt_date["clinicId"]
    apptDate = appt_date["date"]

    #Invoke to get all the booked timing
    appt_time = invoke_http(appt_timing_URL + "/" + str(clinicId) + "/" + str(apptDate))
    print("\n Unavailable timing:", appt_time)

    code = appt_time["code"]
    if code not in range(200,300):
        return jsonify({
            "code": 500,
            "message": "No advanced booking"
        })
    else:
        booked_timing = appt_time["data"]["appointment"]

    return {
        "code":200,
        "data": booked_timing
    }

@app.route("/set_appointment", methods=['POST'])
def check_appointment():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            appt_details = request.get_json()
            print("\n Appointment info in JSON:", appt_details)

            #1. Send appt details to set appointment
            appt_result = set_appointment(appt_details)
            return appt_result

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "setAppointment.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def set_appointment(appt_details):
    #2. Invoke appointmentMS
    appt_result = invoke_http(appt_URL, method = "POST", json = appt_details)
    print("\n Appointment result", appt_result)

    code = appt_result["code"]
    if code not in range(200, 300):
        return {
            "code": 500,
            "message": "Appointment created already"
        }

    else:
        nric = appt_details["nric"]

        #3. Invoke subsidyMS to check for subsidy card
        subsidy_result = invoke_http(subsidy_URL + str(nric))
        print("\n Subsidy result:", subsidy_result)
        
        code = subsidy_result["code"]
        if code not in range(200,300):
            appt_result["data"]["subsidy_status"] = "No subsidy"
            
        else:
            appt_result["data"]["subsidy_status"] = subsidy_result["data"]

        data = appt_result["data"]
        return {
            "code":200,
            "data": data
        }      

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5008, debug=True)