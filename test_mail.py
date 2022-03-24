from mailjet_rest import Client
import os
api_key = 'ce935253e850312f41b9c38c450a9ca0'
api_secret = '3fdd8dcf9fd9bb6cf96bb71d97a659ac'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "bryan.shing.2020@scis.smu.edu.sg",
        "Name": "Bryan"
      },
      "To": [
        {
          "Email": "bryanshing21@gmail.com",
          "Name": "Bryan"
        }
      ],
      "Subject": "Reorder Drug Supplies",
      "TextPart": "Reorder Drugs",
      "HTMLPart": "Dear <b>" + "Drug Supplier Name" + "</b>, <br> Our branch at <b>"+ "Clinic Name" + "</b> has low supplies of <b><u>" + "Drug Name" + "</u></b>. We would like to place an order of <b><u>" + "Quantity" + "</u></b>. Please make the delivery to <b><u>" + "Clinic Address" + "</u></b>.<br><br> Thank you for doing business with us! <br><br>Warm Regards, <br>" + "Clinic Name",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())
