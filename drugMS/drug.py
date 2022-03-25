import os, sys
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class Drug(db.Model):
    __tablename__ = 'drug'
    clinicId = db.Column(db.Numeric(3), primary_key=True, nullable=False)
    drugId = db.Column(db.Integer, nullable=False, primary_key=True)
    drugName = db.Column(db.String(128), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    restockStatus = db.Column(db.String(3), nullable=False)

    def __init__(self, clinicId, drugId, drugName, quantity, restockStatus):
        self.clinicId = clinicId
        self.drugId = drugId
        self.drugName = drugName
        self.quantity = quantity
        self.restockStatus = restockStatus
        
    def json(self):
        return {"clinicId": self.clinicId, "drugName": self.drugName, "drugId": self.drugId, "quantity": self.quantity, "restockStatus": self.restockStatus}


@app.route("/drug")
def get_all():
    druglist = Drug.query.all()
    if len(druglist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "drug": [drug.json() for drug in druglist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no drugs."
        }
    ), 404

@app.route("/drug/<string:clinicId>")
def get_all_drug_by_clinic(clinicId):
    druglist = Drug.query.filter_by(clinicId=clinicId).all()
    if len(druglist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "drug": [drug.json() for drug in druglist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no drugs."
        }
    ), 404
    
@app.route("/drug/<string:clinicId>/<string:drugName>")
def find_by_clinic_drug(clinicId,drugName):
    drug = Drug.query.filter_by(clinicId=clinicId,drugName=drugName).first()
    if drug:
        return jsonify(
            {
                "code": 200,
                "data": drug.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Drug not found."
        }
    ), 404


@app.route("/drug/<string:clinicId>/<string:drugId>", methods=['POST'])
def create_drug(clinicId,drugId):
    if (Drug.query.filter_by(clinicId=clinicId,drugId=drugId).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "drugId": drugId
                },
                "message": "Drug already exists."
            }
        ), 400

    data = request.get_json()
    drug = Drug(drugId, **data)

    try:
        db.session.add(drug)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "clinicId": clinicId,
                    "drugId": drugId
                },
                "message": "An error occurred creating the drug."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": drug.json()
        }
    ), 201


@app.route("/drug/<string:clinicId>/<string:drugName>", methods=['PUT'])
def update_drug(clinicId,drugName):
    drug = Drug.query.filter_by(clinicId=clinicId,drugName=drugName).first()
    if drug:
        data = request.get_json()
        if data['quantity']:
            drug.quantity = data['quantity'] 
        if data['restockStatus']:
            drug.restockStatus = data['restockStatus']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": drug.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "clinicId": clinicId,
                "drugName": drugName
            },
            "message": "Drug not found."
        }
    ), 404


@app.route("/drug/<string:clinicId>/<string:drugName>", methods=['DELETE'])
def delete_drug(clinicId,drugName):
    drug = Drug.query.filter_by(clinicId=clinicId,drugName=drugName).first()
    if drug:
        db.session.delete(drug)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "clinicId": clinicId,
                    "drugName": drugName
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "clinicId": clinicId,
                "drugName": drugName
            },
            "message": "Drug not found."
        }
    ), 404


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage drugs ...")
    app.run(host='0.0.0.0', port=5007, debug=True)
