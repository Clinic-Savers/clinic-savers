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

class Patient_Record(db.Model):
    __tablename__ = 'patient_record'

    nric = db.Column(db.String(9), primary_key=True, nullable=False)
    patient_name = db.Column(db.String(64), nullable=False)
    drug_name = db.Column(db.String(64), primary_key=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    refill_status = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, primary_key=True, nullable=False)

    def __init__(self, nric, patient_name, drug_name, quantity, refill_status, date):
        self.nric = nric
        self.patient_name = patient_name
        self.drug_name = drug_name
        self.quantity = quantity
        self.refill_status = refill_status
        self.date = date

    def json(self):
        return {"nric": self.nric, "patient_name": self.patient_name, "drug_name": self.drug_name, "quantity": self.quantity, "refill_status": self.refill_status, "date": self.date}


@app.route("/patient_record")
def get_all():
    patient_record_list = Patient_Record.query.all()
    if len(patient_record_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "patient_records": [record.json() for record in patient_record_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no patient records."
        }
    ), 404


@app.route("/patient_record/<string:nric>/<string:drug_name>")
def find_by_nric_and_drug(nric,drug_name):
    record = Patient_Record.query.filter_by(nric=nric,drug_name=drug_name).first()
    if record:
        return jsonify(
            {
                "code": 200,
                "data": record.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Patient record not found."
        }
    ), 404


@app.route("/patient_record/<string:nric>", methods=['POST'])
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
    record = Patient_Record(nric, **data)

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


@app.route("/patient_record/<string:nric>/<string:drug_name>/<string:date>", methods=['PUT'])
def update_record(nric,drug_name,date):
    record = Patient_Record.query.filter_by(nric=nric,drug_name=drug_name,date=date).first()
    if record:
        data = request.get_json()
        if data['drug_name']:
            record.drug_name = data['drug_name']
        if data['quantity']:
            record.quantity = data['quantity']
        if data['refill_status']:
            record.refill_status = data['refill_status'] 
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
                "drug_name": drug_name,
                "date": date
            },
            "message": "Patient record not found."
        }
    ), 404


@app.route("/patient_record/<string:nric>/<string:drug_name>/<string:date>", methods=['DELETE'])
def delete_record(nric,drug_name,date):
    record = Patient_Record.query.filter_by(nric=nric,drug_name=drug_name,date=date).first()
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "nric": nric,
                    "drug_name": drug_name,
                    "date": date
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "nric": nric,
                "drug_name": drug_name,
                "date": date
            },
            "message": "Patient record not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
