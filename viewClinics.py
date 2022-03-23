from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

import pika
import json

app = Flask(__name__)
CORS(app)

clinic_URL = "http://localhost:5002/clinic"
distance_URL = "http://localhost:5000/"
#book_URL = "http://localhost:5000/book"
# order_URL = "http://localhost:5001/order"
# shipping_record_URL = "http://localhost:5002/shipping_record"
#activity_log_URL = "http://localhost:5003/activity_log"
#error_URL = "http://localhost:5004/error"


@app.route("/check_dist", methods=['POST'])
def check_dist():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            patientAddress = request.get_json()
            print("\nReceived an order in JSON:", patientAddress)

            # do the actual work
            # 1. Send order info {cart items}
            result = retrieveClinic(patientAddress)
            print('\n------------------------')
            print('\nresult: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "check_dist.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def retrieveClinic(patientAddress):
    # 2. Send the patientAddress to clinic microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    clinic_result = invoke_http(clinic_URL, method='GET', json=patientAddress)
    print('clinic_result:', clinic_result)

    # Check the order result; if a failure, send it to the error microservice.
    code = clinic_result["code"]
    message = json.dumps(clinic_result)

    if code not in range(200, 300):
        return {
            "code": 500,
            "data": {"clinic_result": clinic_result},
            "message": "Clinic search failure"
        }

    else:
        # Send the patientAddress to clinic microservice
        # Invoke the clinic microservice
        clinic_list = invoke_http(clinic_URL, method="GET", json=clinic_result)

        print("clinic_list:", clinic_list)
        # clinic_list is a json with two columns - name, postal cose
        clinic_list = None

        #Invoke distance microservice - send the patientAddress and List of clinics
        distance_result = invoke_http(distance_URL,method="GET",json= clinic_list)

        


    # Check the shipping result;
    # if a failure, send it to the error microservice.
    code = shipping_result["code"]
    if code not in range(200, 300):
        # Inform the error microservice
        #print('\n\n-----Invoking error microservice as shipping fails-----')
        print('\n\n-----Publishing the (shipping error) message with routing_key=shipping.error-----')

        # invoke_http(error_URL, method="POST", json=shipping_result)
        message = json.dumps(shipping_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="shipping.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2))

        print("\nShipping status ({:d}) published to the RabbitMQ Exchange:".format(
            code), shipping_result)

        # 7. Return error
        return {
            "code": 400,
            "data": {
                "order_result": order_result,
                "shipping_result": shipping_result
            },
            "message": "Simulated shipping record error sent for error handling."
        }

    # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "order_result": order_result,
            "shipping_result": shipping_result
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
