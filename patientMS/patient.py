from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/patient'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class Patient(db.Model):
    __tablename__ = 'patient'
    NRIC = db.Column(db.String(64), primary_key=True)
    patientName = db.Column(db.String(64), nullable=False)
    mobileNumber = db.Column(db.Integer)
    address = db.Column(db.String(128), nullable=False)
    vaccinationStatus = db.Column(db.String(64), nullable=False)

    def __init__(self, NRIC, patientName, mobileNumber, address, vaccinationStatus):
        self.NRIC = NRIC
        self.patientName = patientName
        self.mobileNumber = mobileNumber
        self.address = address
        self.vaccinationStatus = vaccinationStatus
        
    def json(self):
        return {"patientName": self.patientName, "NRIC": self.NRIC, "mobileNumber": self.mobileNumber, "address": self.address, "vaccinationStatus": self.vaccinationStatus}


@app.route("/patient")
def get_all():
    patientlist = Patient.query.all()
    if len(patientlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "patient": [patient.json() for patient in patientlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no patients."
        }
    ), 404


@app.route("/patient/<string:NRIC>")
def find_by_NRIC(NRIC):
    patient = Patient.query.filter_by(NRIC=NRIC).first()
    if patient:
        return jsonify(
            {
                "code": 200,
                "data": patient.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Patient not found."
        }
    ), 404


@app.route("/patient/<string:NRIC>", methods=['POST'])
def create_patient(NRIC):
    if (Patient.query.filter_by(NRIC=NRIC).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "NRIC": NRIC
                },
                "message": "Patient already exists."
            }
        ), 400

    data = request.get_json()
    patient = Patient(NRIC, **data)

    try:
        db.session.add(patient)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "NRIC": NRIC
                },
                "message": "An error occurred creating the patient account."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": patient.json()
        }
    ), 201


@app.route("/patient/<string:NRIC>", methods=['PUT'])
def update_patient(NRIC):
    patient = Patient.query.filter_by(NRIC=NRIC).first()
    if patient:
        data = request.get_json()
        if data['patientName']:
            patient.patientName = data['patientName']
        if data['mobileNumber']:
            patient.mobileNumber = data['mobileNumber'] 
        if data['address']:
            patient.address = data['address']     
        if data['vaccinationStatus']:
            patient.vaccinationStatus = data['vaccinationStatus'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": patient.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "NRIC": NRIC
            },
            "message": "Patient not found."
        }
    ), 404


@app.route("/patient/<string:NRIC>", methods=['DELETE'])
def delete_patient(NRIC):
    patient = Patient.query.filter_by(NRIC=NRIC).first()
    if patient:
        db.session.delete(patient)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "NRIC": NRIC
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "NRIC": NRIC
            },
            "message": "Patient not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5222, debug=True)
