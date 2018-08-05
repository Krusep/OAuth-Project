from flask import Flask
from datetime import datetime, timedelta
from random import randint
app = Flask(__name__)


# Authorization server
tokens = {}

@app.route('/authorization') # her skal være login og så redirect tilbage med token
def authorize():
    token = randint(0,10000)
    expiration_date = datetime.now() + timedelta(seconds = 10) # Tokens live for 10 minutes
    tokens[str(token)] = expiration_date
    return '''Username: <input type="text" name="fname"><br>
        Password: <input type="password" name="lname"><br>
        <a href="http://10.192.105.100:5000/logged-in/%s"><button>Log in</button></a>''' % token

# Resource server
@app.route('/resource/<token>') # should redirect back to client w/ resource immediately
def return_resource(token):
    if token in tokens:
        if tokens[token] > datetime.now(): # True if token has not expired
            resource = 'This is your secret resource'
        else:
            resource = 'Your access token has expired'
    else:
        resource = 'Access denied'
        url = 'http://10.192.105.100:5000/final/%s' % resource
    return '<script> window.location = \"%s\" </script>' % url

