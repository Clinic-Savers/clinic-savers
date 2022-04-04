# clinic-savers

## Prerequisites ##

1. To ensure Mailjet api is functioning within Notification microservice, navigate to ```clinic-savers``` directory and enter the following command in command prompt/terminal.

    1. For Windows users

       ```
       pip install mailjet_rest
       ```
    
    2. For Mac users

       ```
       python3 -m pip install mailjet_rest
       ```

2. Before accessing patient login UI, navigate to files directory under patient_login by entering the following command in command prompt/terminal

![First prerequisite](prereq_1.jpg)
<br>

Next, enter the following command

```
npm install
```

<br>
Lastly, to ensure SingPass API is running within our patient login UI - enter the following command

```
.\start.bat
```

## Run the microservices ##

The microservices will be run on localhost. Please make sure you're at the correct directory ```clinic-savers``` before running the commands below.

To run Clinic, run this command in command prompt/terminal
```
python clinic.py
```

To run Distance, run this command in command prompt/terminal
```
python distance.py
```

To run Drug, run this command in command prompt/terminal
```
python drug.py
```

To run Notification, run this command in command prompt/terminal
```
python notification.py
```

To run Patient, run this command in command prompt/terminal
```
python patient.py
```

To run Prescribe Drug, run this command in command prompt/terminal
```
python prescribeDrug.py
```

To run Set Appointment, run this command in command prompt/terminal
```
python setAppointment.py
```

To run Subsidy, run this command in command prompt/terminal
```
python subsidy.py
```

To run View Clinics, run this command in command prompt/terminal
```
python viewClinics.py
```

## Access to Frontend UI ##
add process of user journey (order in which the pages will be accessed)

<br><br>
For the frontend files to function, clinic-savers repository has to be saved in the webroot

![Location of clinic-savers](clinicsaversloc.jpg)

<br><br>
Our frontend webpages can be accessed through these links:

* Clinic login: http://localhost/clinic-savers/frontend/clinicLogin.html
* Patient login: http://localhost:3001
* User type selection: http://localhost/clinic-savers/frontend/user.html
* Appointment booking: http://localhost/clinic-savers/frontend/patientUI.html
* Appointment record: http://localhost/clinic-savers/frontend/viewAppointments.html
* Patient records: http://localhost/clinic-savers/frontend/patientRecords.html
* Drug prescription: http://localhost/clinic-savers/frontend/prescribeDrug.html
* Drug restocking: http://localhost/clinic-savers/frontend/restock.html
* Subsidy card information: http://localhost/clinic-savers/frontend/subsidyCard.html