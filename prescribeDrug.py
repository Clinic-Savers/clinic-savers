from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

patientRecord_URL = "http://localhost:5006/patientRecord/"
drug_URL ="http://localhost:5007/drug/drugName/"
@app.route("/create_record", methods=['POST'])
def create_record():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            patientRecord = request.get_json()
            print("\nReceived an patient record in JSON:", patientRecord)

            # do the actual work
            # 1. Send order info {cart items}
            result = processPatientRecord(patientRecord)
            return result

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "prescribeDrug.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processPatientRecord(patientRecord):
    # 2. Send the order info {cart items}
    # Invoke the order microservice
    print('\n-----Invoking patientRecord microservice-----')
    patient_nric_str = patientRecord['nric']
    del patientRecord['nric']
    print(patientRecord)
    record_result = invoke_http(patientRecord_URL + patient_nric_str , method='POST', json=patientRecord)
    print('record_result:', record_result)


    # Check the order result; if a failure, send it to the error microservice.
    code = record_result["code"]
    if code not in range(200, 300):
        # 7. Return error
        return {
            "code": 500,
            "data": {"record_result": record_result},
            "message": "Patient record creation failure."
        }
        
    print('\n-----Invoking drug microservice-----')
    patient_drug_qty = patientRecord['quantity']
    patient_drugName = patientRecord['drugName']
    drug = invoke_http(drug_URL + patient_drugName , method='GET')
    drug_qty = drug['quantity']
    new_qty = drug_qty - patient_drug_qty
    drug_result = invoke_http(drug_URL + patient_drugName , method='PUT', json={"quantity": new_qty})
    
    code = drug_result["code"]
    if code not in range(200, 300):
        # 7. Return error
        return {
            "code": 500,
            "data": {"drug_result": drug_result},
            "message": "Drug record update failure."
        }
        
    # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "record_result": record_result,
            "drug_result": drug_result
        }
    }



# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for prescribing a drug...")
    app.run(host="0.0.0.0", port=5120, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
