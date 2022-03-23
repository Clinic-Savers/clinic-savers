from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class Clinic(db.Model):
    __tablename__ = 'clinic'
    clinicName = db.Column(db.String(128), nullable=False, primary_key=True)
    clinicAddress = db.Column(db.String(128), nullable=False)
    clinicPostalCode = db.Column(db.Integer, nullable=False, primary_key=True)
    description = db.Column(db.String(128), nullable=False)

    def __init__(self, clinicName, clinicAddress, clinicPostalCode, description):
        self.clinicName = clinicName
        self.clinicAddress = clinicAddress
        self.clinicPostalCode = clinicPostalCode
        self.description= description
    def json(self):
        return {"clinicName": self.clinicName, "clinicAddress": self.clinicAddress, "clinicPostalCode": self.clinicPostalCode, "description": self.description}


@app.route("/clinic")
def get_all():
    cliniclist = Clinic.query.all()
    if len(cliniclist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "clinic": [clinic.json() for clinic in cliniclist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no clinics."
        }
    ), 404


@app.route("/clinic/<string:clinicPostalCode>")
def find_by_clinicPostalCode(clinicPostalCode):
    clinic = Clinic.query.filter_by(clinicPostalCode=clinicPostalCode).first()
    if clinic:
        return jsonify(
            {
                "code": 200,
                "data": clinic.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Clinic not found."
        }
    ), 404
    
@app.route("/clinic/<string:clinicName>")
def find_by_clinicName(clinicName):
    clinic = Clinic.query.filter_by(clinicName=clinicName).first()
    if clinic:
        return jsonify(
            {
                "code": 200,
                "data": clinic.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Clinic not found."
        }
    ), 404


@app.route("/clinic/<string:clinicPostalCode>", methods=['POST'])
def create_clinic(clinicPostalCode):
    if (Clinic.query.filter_by(clinicPostalCode=clinicPostalCode).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "clinicPostalCode": clinicPostalCode
                },
                "message": "Clinic already exists."
            }
        ), 400

    data = request.get_json()
    clinic = Clinic(clinicPostalCode, **data)

    try:
        db.session.add(clinic)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "clinicPostalCode": clinicPostalCode
                },
                "message": "An error occurred creating the clinic."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": clinic.json()
        }
    ), 201


@app.route("/clinic/<string:clinicPostalCode>", methods=['PUT'])
def update_drug(clinicPostalCode):
    clinic = Clinic.query.filter_by(clinicPostalCode=clinicPostalCode).first()
    if clinic:
        data = request.get_json()
        if data['clinicName']:
            clinic.clinicName = data['clinicName']
        if data['clinicAddress']:
            clinic.clinicAddress = data['clinicAddress'] 
        if data['clinicPostalCode']:
            clinic.clinicPostalCode = data['clinicPostalCode'] 
        if data['description']:
            clinic.description = data['description'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": clinic.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "clinicPostalCode": clinicPostalCode
            },
            "message": "Clinic not found."
        }
    ), 404


@app.route("/clinic/<string:clinicPostalCode>", methods=['DELETE'])
def delete_clinic(clinicPostalCode):
    clinic = Clinic.query.filter_by(clinicPostalCode=clinicPostalCode).first()
    if clinic:
        db.session.delete(clinic)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "clinicPostalCode": clinicPostalCode
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "clinicPostalCode": clinicPostalCode
            },
            "message": "Clinic not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
