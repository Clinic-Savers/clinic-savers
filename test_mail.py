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
          "Email": "bryan.shing.2020@scis.smu.edu.sg",
          "Name": "Bryan"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())
