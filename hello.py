from flask import Flask, render_template
from random import randint
app = Flask(__name__)


# Client
@app.route('/') # Skal have knap der sender til auth
def index():
    return '<a href="http://10.192.105.100:5000/authorization"><button>Get authorized!</button></a>'

@app.route('/logged-in/<token>') # Kommer tilbage fra authorization
def fetch_resource(token): # request resource fra resource server vha token
    return '<p> Added token: %s </p> <a href="http://10.192.105.100:5000/resource"><button>Fetch resource</button></a>' % token

@app.route('/final/<resource>')
def display_resource(resource):
    return 'Your resource is: %s' % resource


# Authorization server
tokens = [] # TODO : Make this a dictionary instead to map tokens to expiration times

@app.route('/authorization') # her skal være login og så redirect tilbage med token
def authorize():
    token = randint(0,10000)
    tokens.append(token)
    # return 'Added token: %s' % token
    return '<a href="http://10.192.105.100:5000/logged-in/%s"><button>Log in</button></a>' % token

# Resource server
@app.route('/resource') # should redirect back to client w/ resource immediately
def return_resource():
    resource = randint(0,10)
    url = 'http://10.192.105.100:5000/final/%s' % resource
    return '<script> window.location = \"%s\" </script>' % url
