# importing the Flask class from the flask module
from flask import Flask


#defining the create_app function
def create_app():
    #creating the Flask application
    app = Flask(__name__)

    #returning the Flask application
    return app



