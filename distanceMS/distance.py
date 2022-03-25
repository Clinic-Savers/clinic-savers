from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import invokes 
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

api_key = "AIzaSyC1hytlrSzRCAMd4LK-A0hzQ85IoVZIJpg"


@app.route("/checkDist", methods = ["POST"])
def get_distance():
    data = request.get_json()
    data = json.loads(data)
    print(data)
    
    patient = data["patient"]["patientPostalCode"]
    clinics = data["clinics"]

    clinic_path = ""
    for clinic in clinics:
        clinic_path += "S" + clinic[1] + "%7C"
    clinic_path = clinic_path[:-3]

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=" + clinic_path + "&origins=S" + patient + "&region=sg&key=" + api_key

    result = invokes.invoke_http(url,"GET")

    print(result)

    if result["rows"][0]["elements"][0]["status"] != 'NOT_FOUND':
        return jsonify(
            {
                "code": 200,
                "data": result
            }
        )

    return jsonify(
        { 
            "code": 404,
            "message": "Patient Postal Code cannot be found"
        }
    ), 404    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
