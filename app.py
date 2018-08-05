from flask import Flask, render_template
from random import randint
app = Flask(__name__)


# Client
@app.route('/') # Skal have knap der sender til auth
def index():
    return '<a href="http://10.192.105.100:5000/authorization"><button>Get authorized!</button></a>'

@app.route('/redirected/<token>') # Kommer tilbage fra authorization
def fetch_resource(token): # request resource fra resource server vha token
    return 'Added token: %s' % token


# Authorization server
tokens = [] # TODO : Make this a dictionary instead to map tokens to expiration times

@app.route('/authorization') # her skal være login og så redirect tilbage med token
def authorize():
    token = randint(0,10000)
    tokens.append(token)
    # return 'Added token: %s' % token
    return render_template('authorization.html')

# Resource server
