##### Part 1 - Launching basic app on local machine #####

## Terminal commands to set up flask virtual environment


'python3 -m venv ~/.venvs/flask'

'source ~/.venvs/flask/bin/activiate'

'pip3 install flask'

'pip freeze > requirements.txt' ## Many of the packages that were documented with pip freeze are not the focus right now
## Flask will be the only necessary import
## the appropriate version is documented

## Imports

from flask import Flask


## Setting up basic app pages, routes and endpoints


app = Flask(__name__)

@app.route('/') ## We'll leave only a front slash here and no name so that the default navigation takes us here
def home():
    return 'Welcome to NuForm Patient Portal'

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

## here we try to include examples of pages that would be pertinent for a working and efficient patient portal

## it's important here that as we use def to describe the pages, we also match the endpoints in app.route as well
## the only exception is the home page since its endpoint is described with the default '/'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80) ## though given the option to change the port, we'll leave it as 80. 80 is the default when accessing local host which may simplify the process