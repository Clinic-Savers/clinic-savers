import os, sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class PatientRecord(db.Model):
    __tablename__ = 'patientRecord'

    nric = db.Column(db.String(9), primary_key=True, nullable=False)
    patientName = db.Column(db.String(64), nullable=False)
    drugName = db.Column(db.String(128), primary_key=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    refillStatus = db.Column(db.String(64), nullable=False)
    date = db.Column(db.String(64), primary_key=True, nullable=False)
    time = db.Column(db.String(64), primary_key=True, nullable=False)

    def __init__(self, nric, patientName, drugName, quantity, refillStatus, date, time):
        self.nric = nric
        self.patientName = patientName
        self.drugName = drugName
        self.quantity = quantity
        self.refillStatus = refillStatus
        self.date = date
        self.time = time

    def json(self):
        return {"nric": self.nric, "patientName": self.patientName, "drugName": self.drugName, "quantity": self.quantity, "refillStatus": self.refillStatus, "date": self.date, "time": self.time}


@app.route("/patientRecord")
def get_all_patient_record():
    patient_record_list = PatientRecord.query.all()
    if len(patient_record_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "PatientRecords": [record.json() for record in patient_record_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no patient records."
        }
    ), 404


@app.route("/patientRecord/<string:nric>/<string:drugName>")
def find_patient_record_by_nric_and_drug(nric,drugName):
    record_list = PatientRecord.query.filter_by(nric=nric,drugName=drugName).all()
    if len(record_list):
        return jsonify(
            {
                "code": 200,
                "PatientRecord": [record.json() for record in record_list]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Patient record not found."
        }
    ), 404


@app.route("/patientRecord/<string:nric>", methods=['POST'])
def create_patient_record(nric):
    # if (Patient_Record.query.filter_by(date=date).first()):
    #     return jsonify(
    #         {
    #             "code": 400,
    #             "data": {
    #                 "date": date
    #             },
    #             "message": "Create"
    #         }
    #     ), 400

    data = request.get_json()
    record = PatientRecord(nric, **data)
    print(record)

    try:
        db.session.add(record)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "nric": nric
                },
                "message": "An error occurred creating the patient record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": record.json()
        }
    ), 201


@app.route("/patientRecord/<string:nric>/<string:drugName>/<string:date>/<string:time>", methods=['PUT'])
def update_patient_record(nric,drugName,date,time):
    record = PatientRecord.query.filter_by(nric=nric,drugName=drugName,date=date,time=time).first()
    if record:
        data = request.get_json()
        if data['drugName']:
            record.drugName = data['drugName']
        if data['quantity']:
            record.quantity = data['quantity']
        if data['refillStatus']:
            record.refillStatus = data['refillStatus'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": record.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "nric": nric,
                "drugName": drugName,
                "date": date,
                "time" : time
            },
            "message": "Patient record not found."
        }
    ), 404


@app.route("/patientRecord/<string:nric>/<string:drugName>/<string:date>/<string:time>", methods=['DELETE'])
def delete_patient_record(nric,drugName,date,time):
    record = PatientRecord.query.filter_by(nric=nric,drugName=drugName,date=date,time=time).first()
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "nric": nric,
                    "drugName": drugName,
                    "date": date,
                    "time" : time
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "nric": nric,
                "drugName": drugName,
                "date": date,
                "time" : time
            },
            "message": "Patient record not found."
        }
    ), 404


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": patient records ...")
    app.run(host='0.0.0.0', port=5006, debug=True)
