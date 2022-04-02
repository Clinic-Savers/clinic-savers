from datetime import date, time, datetime, timedelta
from sqlite3 import Date
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from sqlalchemy import func 
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
 
CORS(app) 

class Appointment(db.Model):
    __tablename__ = 'appointment'
    nric = db.Column(db.String(9), nullable=False, primary_key=True)
    symptoms = db.Column(db.String(128), nullable=False)
    clinicId = db.Column(db.Numeric(3), nullable=False)
    appointmentDate = db.Column(db.String(64), nullable=False, primary_key=True)
    appointmentTime = db.Column(db.String(64), nullable=False, primary_key=True)    

    def __init__(self, nric, symptoms, clinicId, appointmentDate, appointmentTime):
        self.nric = nric
        self.symptoms = symptoms
        self.clinicId = clinicId
        self.appointmentDate = appointmentDate
        self.appointmentTime = appointmentTime
        
        
    def json(self):
        return {"nric": self.nric, "symptoms": self.symptoms, "clinicId": self.clinicId, "appointmentDate": self.appointmentDate, "appointmentTime": self.appointmentTime}

# @app.route("/appointment/<string:clinicID>/<string: appointDate>")
# def check_appt_timing(clinicId, appointDate):
#     clinicId = int(clinicId)
#     appt_list = Appointment.query.filter(Appointment.clinicId.like(clinicId), func.date(Appointment.appointmentDate)==appointDate)
#     if len(appt_list):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "appointment": [appointment.json() for appointment in appt_list]
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "There are no appointments."
#         }
#     ), 404


# get queue length of specified clinic id 
@app.route("/appointment/<string:clinicId>")
def get_queue_length(clinicId): 
    clinicId = int(clinicId)
    now = datetime.now()
    current_time = time(now.hour, now.minute, now.second)
    this = Appointment.query.filter(Appointment.clinicId.like(clinicId), func.date(Appointment.appointmentDate)==date.today(), func.time(Appointment.appointmentTime)>=current_time).count()
    
    if this:
        return jsonify(
            {
                "code": 200,
                "data": {"queueLength": this}
            }
        )
    return jsonify(
        { 
            "code": 404,
            "message": "No queue."
        }
    ), 404    

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
def find_by_appointmentDate(nric, appointmentDate):
    appointment = Appointment.query.filter_by(nric=nric, appointmentDate=appointmentDate).first()
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


@app.route("/set_appointment", methods=["POST"])
def set_appointment():
    data = request.get_json()

    #retrieve the details
    nric = data["nric"]
    symptoms = data["symptoms"]
    clinicId = int(data["clinicId"])

    #Check the lastest appointment time
    now = datetime.now()
    current_time = time(now.hour, now.minute, now.second)
    last_appt = Appointment.query.filter(Appointment.clinicId.like(clinicId), func.date(Appointment.appointmentDate)==date.today()>=current_time).first()

    #No appointment made after the current timing
    if last_appt == None:
        if current_time.minute > 30:
            newTiming = time(current_time.hour + 1,0,0)
        else: 
            newTiming = time(current_time.hour,30,0)

        appointmentDate = date.today()

    #Find next available timing
    else:
        format = "%H:%M:%S"
        last_timing = datetime.strptime(last_appt.appointmentTime,format)

        newTiming= last_timing + timedelta(minutes=30)
        newTiming = newTiming.strftime(format)

        appointmentDate = last_appt.appointmentDate

    appointment = Appointment(nric, symptoms, clinicId, appointmentDate, newTiming)
    
    try:
        db.session.add(appointment)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "Appointment made already"
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
    app.run(host='0.0.0.0', port=5003, debug=True)
