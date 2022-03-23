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

class DrugRefill(db.Model):
    __tablename__ = 'drugRefill'

    nric = db.Column(db.String(9), primary_key=True)
    patientName = db.Column(db.String(128), nullable=False)
    existingCondition = db.Column(db.String(64), nullable=False)
    drugName = db.Column(db.String(64), nullable=False)
    date = db.Column(db.String(64), nullable=False)

    def __init__(self, nric, patientName, existingCondition, drugName, date):
        self.nric = nric
        self.patientName = patientName
        self.existingCondition = existingCondition
        self.drugName = drugName
        self.date = date

    def json(self):
        return {"nric": self.nric, "patientName": self.patientName, "existingCondition": self.existingCondition, "drugName": self.drugName, "date": self.date}


@app.route("/drugRefill")
def get_all_drug_refill_record():
    refill_record = DrugRefill.query.all()
    if len(refill_record):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Drug Refill Records": [record.json() for record in refill_record]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no drug refill records."
        }
    ), 404


@app.route("/book/<string:nric>/<string:drugName>")
def find_drug_refill_record_by_nric_and_drug(nric,drugName):
    record = DrugRefill.query.filter_by(nric=nric,drugName=drugName).first()
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
            "message": "Drug refill record not found."
        }
    ), 404


@app.route("/book/<string:nric>", methods=['POST'])
def create_drug_refill_record(nric):
    # if (Book.query.filter_by(isbn13=isbn13).first()):
    #     return jsonify(
    #         {
    #             "code": 400,
    #             "data": {
    #                 "isbn13": isbn13
    #             },
    #             "message": "Book already exists."
    #         }
    #     ), 400

    data = request.get_json()
    record = DrugRefill(nric, **data)

    try:
        db.session.add(record)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "nric": nric
                },
                "message": "An error occurred creating the drug refill record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": record.json()
        }
    ), 201


@app.route("/book/<string:nric>/<string:drugName>/<string:date>", methods=['PUT'])
def update_drug_refill_record(nric,drugName,date):
    record = DrugRefill.query.filter_by(nric=nric,drugName=drugName,date=date).first()
    if record:
        data = request.get_json()
        if data['existingCondition']:
            record.existingCondition = data['existingCondition']
        if data['drugName']:
            record.drugName = data['drugName']
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
                "nric": nric,
                "drugName": drugName,
                "date": date
            },
            "message": "Drug Refill Record not found."
        }
    ), 404


@app.route("/book/<string:nric>/<string:drugName>/<string:date>", methods=['DELETE'])
def delete_drug_refill_record(nric,drugName,date):
    record = DrugRefill.query.filter_by(nric=nric,drugName=drugName,date=date).first()
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "nric": nric,
                    "drugName": drugName,
                    "date": date
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "nric": nric,
                "drugName": drugName,
                "date": date
            },
            "message": "Drug Refill Record not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
