from operator import itemgetter
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json

app = Flask(__name__)
CORS(app)

appt_URL = "http://192.168.1.108:5003/set_appointment"
patient_URL = "http://192.168.1.108:5000/patient/"

@app.route("/set_appt", methods=['POST'])
def receive_clinic():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            selected_clinic = request.get_json()
            print("\nReceived postal code in JSON:", selected_clinic)

            result = set_appt(selected_clinic)
            return result

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "check_dist.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def set_appt(selectedClinic):
    print("Setting appointment...")
    patient_info = invoke_http(patient_URL + str(selectedClinic["nric"]))

    code = patient_info["code"]
    if code not in range(200, 300):
        return {
            patient_info
        }

    else:
        create_appt = {"nric": patient_info["data"]["nric"], 
                        "name": patient_info["data"]["patientName"],
                        "symptoms": "NIL",
                        "potentialCovid": "NIL",
                        "clinicId": selectedClinic["clinic"]
                        }

        create_appt = json.dumps(create_appt)

        appt_result = invoke_http(appt_URL, method = "POST", json=create_appt)

        code = appt_result["code"]
        
        if code not in range(200, 300):
            return {
                "code": 500,
                "data": {"set_appt result": appt_result },
                "message": "Clinic search failure"
            }

        else:
            
            data = appt_result["data"]
            return {
                "code":200,
                "data": data
            }        

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5008, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
