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
    drugId = db.Column(db.Integer, nullable=False, primary_key=True)
    drugName = db.Column(db.String(128), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, drugId, drugName, quantity):
        self.drugId = drugId
        self.drugName = drugName
        self.quantity = quantity
        
    def json(self):
        return {"drugName": self.drugName, "drugId": self.drugId, "quantity": self.quantity}


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


@app.route("/drug/drugId/<string:drugId>")
def find_by_drugId(drugId):
    drug = Drug.query.filter_by(drugId=drugId).first()
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
    
@app.route("/drug/drugName/<string:drugName>")
def find_by_drugName(drugName):
    drug = Drug.query.filter_by(drugName=drugName).first()
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


@app.route("/drug/<string:drugId>", methods=['POST'])
def create_drug(drugId):
    if (Drug.query.filter_by(drugId=drugId).first()):
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


@app.route("/drug/<string:drugId>", methods=['PUT'])
def update_drug(drugId):
    drug = Drug.query.filter_by(drugId=drugId).first()
    if drug:
        data = request.get_json()
        if data['drugName']:
            drug.drugName = data['drugName']
        if data['quantity']:
            drug.quantity = data['quantity'] 
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
                "drugId": drugId
            },
            "message": "Drug not found."
        }
    ), 404


@app.route("/drug/<string:drugId>", methods=['DELETE'])
def delete_drug(drugId):
    drug = Drug.query.filter_by(drugId=drugId).first()
    if drug:
        db.session.delete(drug)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "drugId": drugId
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "drugId": drugId
            },
            "message": "Drug not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5422, debug=True)
