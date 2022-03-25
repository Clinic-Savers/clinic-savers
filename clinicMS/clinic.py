from tokenize import String
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)  

class Clinic(db.Model):
    __tablename__ = 'clinic'
    id = db.Column(db.Numeric(3), nullable=False, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False, primary_key=True)
    postalCode = db.Column(db.String(6), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self, id, name, address, postalCode, email):
        self.id = id
        self.name = name
        self.address = address
        self.postalCode= postalCode
        self.email = email
    def json(self):
        return {"id": self.id, "name": self.name, "address": self.address, "postalCode": self.postalCode, "email": self.email}


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

@app.route("/clinic/postal/<string:patientPostalCode>")
def find_by_patientPostalCode(patientPostalCode):
    district = patientPostalCode[:2]
    clinicsListByDistrict = Clinic.query.filter(Clinic.postalCode.startswith(district)).all()

    if clinicsListByDistrict:
        return jsonify(
            {
                "code": 200, 
                "data": {
                    "clinic": [clinic.json() for clinic in clinicsListByDistrict]
                }
            }
        )  
    return jsonify(
        {
            "code": 404, 
            "message": "There are no matching clinics."
        }
    )
    
@app.route("/clinic/<string:name>")
def find_by_clinicName(name):
    clinic = Clinic.query.filter_by(name=name).first()
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


#cannot create with just postal code
@app.route("/clinic/<int:id>", methods=['POST'])
def create_clinic(id):
    if (Clinic.query.filter_by(id=id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "id": id
                },
                "message": "Clinic already exists."
            }
        ), 400

    data = request.get_json()
    clinic = Clinic(id, **data)

    try:
        db.session.add(clinic)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "id": id
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


# primary key is now clinicId, so this one need to change?
@app.route("/clinic/<int:id>", methods=['PUT'])
def update_clinic(id):
    clinic = Clinic.query.filter_by(id=id).first()
    if clinic:
        data = request.get_json()
        if data['id']:
            clinic.id = data['id']
        if data['name']:
            clinic.name = data['name'] 
        if data['address']:
            clinic.address = data['address'] 
        if data['postalCode']:
            clinic.postalCode = data['postalCode'] 
        if data['email']:
            clinic.email = data['email']
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
                "id": id
            },
            "message": "Clinic not found."
        }
    ), 404


@app.route("/clinic/<int:id>", methods=['DELETE'])
def delete_clinic(id):
    clinic = Clinic.query.filter_by(id=id).first()
    if clinic:
        db.session.delete(clinic)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "id": id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "id": id
            },
            "message": "Clinic not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
