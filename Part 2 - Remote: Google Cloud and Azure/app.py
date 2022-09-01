## Terminal commands

'apt-get install updates' ## installs updates for vm

'sudo apt install python3-pip' ##installs pip 

'python3 app.py' ## runs the application

'sudo nohup python3 app.py > log.txt 2>&1 &' ## this terminal command ensures that the app runs in the background even when the client is shut down



## Imports

from flask import Flask


## We keep the same script as from Part 1 - with a small difference in line 37


app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/scheduleappointments') 
def scheduleappointments():
    return 'Schedule Appointments'

@app.route('/healthinformation')
def healthinformation():
    return 'View Health History, Past Appointments, or Update Your Health Information'

@app.route('/makeapayment')
def makeapayment():
    return 'View Bills or Make a Payment'

@app.route('/prescriptions')
def prescriptions():
    return 'Check Drug Refills and Requests'

@app.route('/contact')
def contact():
    return 'Contact Your Primary Care Physician'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) ## here we can set host as the exact external ip of the remote environment, but since we are deploying on two environments, we can simply leave it as 0.0.0.0 to match whatever ip is given by either