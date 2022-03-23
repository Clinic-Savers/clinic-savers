from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/subsidy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app) 

class Subsidy(db.Model):
    __tablename__ = 'subsidy'
    nric = db.Column(db.String(9), nullable=False, primary_key=True)
    cardNumber = db.Column(db.String(64), nullable=False)
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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)