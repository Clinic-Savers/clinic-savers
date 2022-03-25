from operator import itemgetter
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import json

app = Flask(__name__)
CORS(app)

clinic_URL = "http://localhost:5002/clinic/postal/"
distance_URL = "http://192.168.1.108:5001/checkDist"
appointment_URL = "http://localhost:5003/appointment/"

@app.route("/check_dist", methods=['POST'])
def check_dist():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            patientPostalCode = request.get_json()
            print("\nReceived postal code in JSON:", patientPostalCode)

            result = retrieveClinic(patientPostalCode)
            # print('\n------------------------')
            # print('\nresult: ', patientPostalCode)
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


def retrieveClinic(patientPostalCode):
    # 2. Send the patientAddress to clinic microservice
    
    patientPostalCode_str = patientPostalCode["patientPostalCode"]
    clinic_result = invoke_http(clinic_URL + patientPostalCode_str, method='GET', json=patientPostalCode)
    print('clinic_result:', clinic_result)

    code = clinic_result["code"]
    clinics = clinic_result["data"]["clinic"]
    
    patient_clinic_postalCode = { 
        "patient": patientPostalCode,
        "clinics": [] }


    for clinic in clinics:
        patient_clinic_postalCode["clinics"].append([clinic["id"], clinic["name"] ,clinic["postalCode"]])

    #convert to JSON format
    patient_clinic_postalCode = json.dumps(patient_clinic_postalCode)
    
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"clinic_result": clinic_result},
            "message": "Clinic search failure"
        }

    else:
        #Invoke distance microservice - send the patientAddress and List of clinics
        distance_result = invoke_http(distance_URL,method="POST",json= patient_clinic_postalCode)
        
        print("\ndistance result:", distance_result)
        code = distance_result["code"]

        if code not in range(200, 300):
            return {
                "code": 500,
                "data": {"distance_result": distance_result},
                "message": "Distance search fail"
            }

        else:
            data = distance_result["data"]
            distance_compare = data["rows"][0]["elements"]
            sort_dist = {}

            for i in range(0,len(clinics)):
                sort_dist[clinics[i]["id"]] = [clinics[i]["name"], clinics[i]["postalCode"], distance_compare[i]["distance"]["value"]] 
            
            print("\nsort dist", sort_dist)
            # sort_dist = sorted(sort_dist, key=itemgetter(2))

            for clinic in clinics:
                url = appointment_URL + str(clinic["id"])
                appointment_result = invoke_http(url)
                print("\nqueue",appointment_result)

                code = appointment_result["code"]

                if code in range(200, 300):
                    queueLength = appointment_result["data"]["queueLength"]
                    sort_dist[clinic["id"]].append(queueLength)
                else:
                    sort_dist[clinic["id"]].append(0)

            sort_dist = sorted(sort_dist.items(), key= lambda x: x[1][2] )
        
            return {
                "code":200,
                "data": sort_dist
            }
        

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
