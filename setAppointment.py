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
subsidy_URL = "http://192.168.1.108:5004/subsidy/"

@app.route("/set_appointment", methods=['POST'])
def check_appointment():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            appt_details = request.get_json()
            print("\n Appointment info in JSON:", appt_details)

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
    appt_result = invoke_http(appt_URL, method = "POST", json = appt_details)
    
    code = appt_result["code"]
    print("appt result", appt_result)
    if code not in range(200, 300):
        return {
            "code": 500,
            "message": "Create appointment fail"
        }

    else:
        nric = appt_details["nric"]
        check_subsidy = invoke_http(subsidy_URL + str(nric))

        if check_subsidy["data"]:
            appt_result["data"]["subsidy_status"] = True
            
        else:
            appt_result["data"]["subsidy_status"] = False

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
