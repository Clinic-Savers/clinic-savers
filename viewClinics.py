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
distance_URL = "http://localhost:5001/checkDist"
appointment_URL = "http://localhost:5003/appointment/"

@app.route("/viewClinics/<string:patientPostalCode>")
def viewClinics(patientPostalCode):
    # patientPostalCode is in string type
    print("\nReceived postal code in JSON:", patientPostalCode)

    listOfClinics = retrieveClinics(patientPostalCode)
    
    return listOfClinics


def retrieveClinics(patientPostalCode):
    # 2. Send the patientPostalCode to clinicMS to get all the clinics in the region
    clinic_result = invoke_http(clinic_URL + patientPostalCode)
    print('clinic_result:', clinic_result)

    code = clinic_result["code"]
    
    #check if it is able to retrieve clinics
    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"clinic_result": clinic_result},
            "message": "Clinic search failure"
        }

    # clinics retrieved
    else:
        clinics = clinic_result["data"]["clinic"]
    
        #create Python object to send to distanceMS
        check_distance = { 
            "patient": patientPostalCode,
            "clinics": [] 
            }
        for clinic in clinics:
            check_distance["clinics"].append([clinic["id"], clinic["name"] ,clinic["postalCode"]])

        #convert Python to JSON format
        check_distance = json.dumps(check_distance)
        
        #Invoke distance microservice
        distance_result = invoke_http(distance_URL, method="POST", json = check_distance)
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

            #rearrange the data retrieved
            sort_dist = {}
            for i in range(0,len(clinics)):
                sort_dist[clinics[i]["id"]] = [clinics[i]["name"], clinics[i]["postalCode"], distance_compare[i]["distance"]["value"]] 
            print("\nClinic's distance", sort_dist)

            #Invoke appointmentMS to get the queue length for each clinic
            for clinic in clinics:
                url = appointment_URL + str(clinic["id"])
                appointment_result = invoke_http(url)

                code = appointment_result["code"]

                #No queue 
                if code not in range(200, 300):
                    sort_dist[clinic["id"]].append(0)
                #Have queue
                else:
                    queueLength = appointment_result["data"]["queueLength"]
                    sort_dist[clinic["id"]].append(queueLength)

            #sort by distance
            sorted_dist = sorted(sort_dist.items(), key= lambda x: x[1][2] )
            
            return {
                "code":200,
                "data": sorted_dist
            }
        

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
