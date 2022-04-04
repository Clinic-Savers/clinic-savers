# clinic-savers

## Prerequisites ##
Before accessing patient login UI, navigate to files directory under patient_login by entering the following command in command prompt/terminal

![First prerequisite](prereq_1.jpg)

Next, enter the following command

```
npm install
```

Lastly, to ensure SingPass API is running within our patient login UI - enter the following command

```
.\start.bat
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