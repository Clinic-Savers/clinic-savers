from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
from os import environ

app = Flask(__name__)
<<<<<<< Updated upstream
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/subsidy'
=======
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
>>>>>>> Stashed changes
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
        
        if (int(expiryyear) + int(expirymonth) + int(expiryday)) <= (int(currentyear) + int(currentmonth) + int(currentday)):
            return jsonify (
                {
                    "code": 200,
                    "data" : False #Subsidy card has expired, not valid
                })
        else:
            return jsonify (
                {
                    "code": 404,
                    "data": True #Subsidy card still valid
                })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)