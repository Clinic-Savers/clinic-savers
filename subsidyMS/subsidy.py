from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app) 

class Subsidy(db.Model):
    __tablename__ = 'subsidy'
    cardNumber = db.Column(db.String(64), nullable=False, primary_key=True)
    nric = db.Column(db.String(9), nullable=False)
    cardType = db.Column(db.Integer, nullable=False)
    organisationType = db.Column(db.String(128), nullable=True)
    expiryDate = db.Column(db.String(64), nullable=False)

    def __init__(self, nric, cardNumber, cardType, organisationType, expiryDate):
        self.nric = nric
        self.cardNumber = cardNumber
        self.cardType = cardType
        self.organisationType = organisationType
        self.expiryDate = expiryDate
        
    def json(self):
        return {"nric": self.nric, "cardNumber": self.cardNumber, "cardType": self.cardType, "organisationType": self.organisationType, "expiryDate": self.expiryDate,}


@app.route("/subsidy/<string:nric>")
def verify_subsidy(nric):
    patient = Subsidy.query.filter_by(nric=nric).first()
    if patient:
        currentDate = date.today().strftime("%d/%m/%Y")
        currentyear = currentDate[6:10]
        currentmonth = currentDate[3:5]
        currentday = currentDate[0:2] 

        expiryyear = patient.expiryDate[6:10]
        expirymonth = patient.expiryDate[3:5]
        expiryday = patient.expiryDate[0:2]

        check = True
        
        if (int(expiryyear) + int(expirymonth) + int(expiryday)) <= (int(currentyear) + int(currentmonth) + int(currentday)):
            check = False

        return jsonify (
            {
                "code": 200,
                "data" : check
            })
        
                
    return jsonify(
        {
            "code": 404,
            "message": "Patient not found."
        }
    ), 404

@app.route("/subsidy/<string:nric>")
def find_by_nric(nric):
    subsidy = Subsidy.query.filter_by(nric=nric).first()

    if subsidy:
        return jsonify(
            {
                "code": 200,
                "data": subsidy.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Patient not found."
        }
    ), 404

@app.route("/subsidy/<string:cardNumber>", methods=['POST'])
def create_subsidy(cardNumber):
    if (Subsidy.query.filter_by(cardNumber=cardNumber).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "cardNumber": cardNumber
                },
                "message": "Card already exists."
            }
        ), 400

    data = request.get_json()
    subsidy = Subsidy(cardNumber, **data)

    try:
        db.session.add(subsidy)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "cardNumber": cardNumber
                },
                "message": "An error occurred adding the subsidy card."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": subsidy.json()
        }
    ), 201

@app.route("/subsidy/<string:cardNumber>", methods=['PUT'])
def update_subsidy(cardNumber):
    subsidy = Subsidy.query.filter_by(cardNumber=cardNumber).first()
    if subsidy:
        data = request.get_json()
        if data['nric']:
            subsidy.nric = data['nric']
        if data['cardType']:
            subsidy.cardType = data['cardType'] 
        if data['organisationType']:
            subsidy.organisationType = data['organisationType']     
        if data['expiryDate']:
            subsidy.expiryDate = data['expiryDate'] 

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": subsidy.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "cardNumber": cardNumber
            },
            "message": "Card not found."
        }
    ), 404


@app.route("/subsidy/<string:cardNumber>", methods=['DELETE'])
def delete_subsidy(cardNumber):
    subsidy = Subsidy.query.filter_by(cardNumber=cardNumber).first()
    if subsidy:
        db.session.delete(subsidy)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "cardNumber": cardNumber
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "cardNumber": cardNumber
            },
            "message": "Card not found."
        }
    ), 404




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)