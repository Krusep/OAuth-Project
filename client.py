from flask import Flask
app = Flask(__name__)


# Client
@app.route('/') # Skal have knap der sender til auth
def index():
    return '<a href="http://10.100.100.100:5000/authorization"><button>Get authorized!</button></a>' # Replace with your IP address

@app.route('/logged-in/<token>') # Kommer tilbage fra authorization
def fetch_resource(token): # request resource fra resource server vha token
    url = '\"http://10.100.100.100:5000/resource/%s\"' % token
    return '<p> Added token: ' + token + '</p> <a href=' + url + '><button>Fetch resource</button></a>'

@app.route('/final/<resource>')
def display_resource(resource):
    return 'Your resource is: %s' % resource
