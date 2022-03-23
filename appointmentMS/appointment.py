from datetime import date
from sqlite3 import Date
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class Appointment(db.Model):
    __tablename__ = 'appointment'
    nric = db.Column(db.String(9), nullable=False, primary_key=True)
    appointmentName = db.Column(db.String(64), nullable=False)
    symptoms = db.Column(db.String(128), nullable=False)
    potentialCovid = db.Column(db.String(3), nullable=False)
    appointmentDate = db.Column(db.String(64), nullable=False, primary_key=True)
    appointmentTime = db.Column(db.String(64), nullable=False, primary_key=True)


    def __init__(self, nric, appointmentName, symptoms, potentialCovid, appointmentDate, appointmentTime):
        self.nric = nric
        self.appointmentName = appointmentName
        self.symptoms = symptoms
        self.potentialCovid = potentialCovid
        self.appointmentDate = appointmentDate
        self.appointmentTime = appointmentTime
        
        
    def json(self):
        return {"appointmentName": self.appointmentName, "nric": self.nric, "symptoms": self.symptoms, "potentialCovid": self.potentialCovid, "appointmentDate": self.appointmentDate, "appointmentTime": self.appointmentTime}


@app.route("/appointment")
def get_all():
    appointmentlist = Appointment.query.all()
    if len(appointmentlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "appointment": [appointment.json() for appointment in appointmentlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no appointments."
        }
    ), 404


@app.route("/appointment/<string:nric>")
def find_by_nric(nric):
    appointment = Appointment.query.filter_by(nric=nric).first()
    if appointment:
        return jsonify(
            {
                "code": 200,
                "data": appointment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Appointment not found."
        }
    ), 404
    
@app.route("/appointment/<string:nric>/<string:appointmentDate>")
def find_by_nric(nric, appointmentDate):
    appointment = Appointment.query.filter_by(nric=nric, date=date).first()
    if appointment:
        return jsonify(
            {
                "code": 200,
                "data": appointment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Appointment not found."
        }
    ), 404


@app.route("/appointment/<string:nric>", methods=['POST'])
def create_appointment(nric):
    appointment = Appointment.query.filter_by(nric=nric).first()
    # if (appointment.query.filter_by(nric=nric).first()):
    #     return jsonify(
    #         {
    #             "code": 400,
    #             "data": {
    #                 "nric": nric
    #             },
    #             "message": "Appointment already exists."
    #         }
    #     ), 400

    data = request.get_json()
    appointment = Appointment(nric, **data)

    try:
        db.session.add(appointment)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "nric": nric
                },
                "message": "An error occurred creating the appointment."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": appointment.json()
        }
    ), 201


@app.route("/appointment/<string:nric>/<string:appointmentDate>/<string:appointmentTime>", methods=['PUT'])
def update_appointment(nric, appointmentDate, appointmentTime):
    appointment = Appointment.query.filter_by(nric=nric, appointmentDate=appointmentDate, appointmentTime=appointmentTime).first()
    if appointment:
        data = request.get_json()
        if data['appointmentTime']:
            appointment.appointmentTime = data['appointmentTime']     
        if data['appointmentDate']:
            appointment.appointmentDate = data['appointmentDate'] 
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": appointment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "nric": nric,
                "appointmentDate": appointmentDate,
                "appointmentTime": appointmentTime
            },
            "message": "Appointment not found."
        }
    ), 404


@app.route("/appointment/<string:nric>/<string:appointmentDate>/<string:appointmentTime>", methods=['DELETE'])
def delete_appointment(nric,appointmentDate,appointmentTime):
    appointment = Appointment.query.filter_by(nric=nric, appointmentDate=appointmentDate, appointmentTime=appointmentTime).first()
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "nric": nric,
                    "appointmentDate": appointmentDate,
                    "appointmentTime": appointmentTime
                }
            }
        )
    return jsonify(
        {
           "code": 404,
            "data": {
                "nric": nric,
                "appointmentDate": appointmentDate,
                "appointmentTime": appointmentTime
            },
            "message": "appointment not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5222, debug=True)
