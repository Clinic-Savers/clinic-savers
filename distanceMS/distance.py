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

class Distance(db.Model):
    __tablename__ = 'distance'

    patientPostalCode = db.Column(db.String(6), primary_key=True, nullable=False)
    clinicPostalCode = db.Column(db.String(6), primary_key=True, nullable=False)
    distanceAway = db.Column(db.String(5), nullable=False)

    def __init__(self, patientPostalCode, clinicPostalCode, distanceAway):
        self.patientPostalCode = patientPostalCode
        self.clinicPostalCode = clinicPostalCode
        self.distanceAway = distanceAway

    def json(self):
        return {"patientPostalCode": self.patientPostalCode, "clinicPostalCode": self.clinicPostalCode, "distanceAway": self.distanceAway}


@app.route("/distance")
def get_all_distance():
    distance_list = Distance.query.all()
    if len(distance_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Distance Records": [record.json() for record in distance_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no distance records."
        }
    ), 404


@app.route("/distance/<string:patientPostalCode>/<string:clinicPostalCode>")
def find_distance_by_patient_and_clinic_postal(patientPostalCode,clinicPostalCode):
    record = Distance.query.filter_by(patientPostalCode=patientPostalCode,clinicPostalCode=clinicPostalCode).first()
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
            "message": "Distance record not found."
        }
    ), 404


@app.route("/distance/<string:patientPostalCode>", methods=['POST'])
def create_distance_record(patientPostalCode):
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
    record = Distance(patientPostalCode, **data)

    try:
        db.session.add(record)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "patientPostalCode": patientPostalCode
                },
                "message": "An error occurred creating the distance record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": record.json()
        }
    ), 201


@app.route("/distance/<string:patientPostalCode>/<string:clinicPostalCode>", methods=['PUT'])
def update_distance_record(patientPostalCode,clinicPostalCode):
    record = Distance.query.filter_by(patientPostalCode=patientPostalCode,clinicPostalCode=clinicPostalCode).first()
    if record:
        data = request.get_json()
        if data['distanceAway']:
            record.distanceAway = data['distanceAway']
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
                "patientPostalCode": patientPostalCode,
                "clinicPostalCode": clinicPostalCode,
            },
            "message": "Distance record not found."
        }
    ), 404


@app.route("/distance/<string:patientPostalCode>/<string:clinicPostalCode>", methods=['DELETE'])
def delete_distance_record(patientPostalCode,clinicPostalCode):
    record = Distance.query.filter_by(patientPostalCode=patientPostalCode,clinicPostalCode=clinicPostalCode).first()
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "patientPostalCode": patientPostalCode,
                    "clinicPostalCode": clinicPostalCode,
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "patientPostalCode": patientPostalCode,
                "clinicPostalCode": clinicPostalCode,
            },
            "message": "Distance record not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
