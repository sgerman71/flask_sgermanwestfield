from flask import Flask, g

# Import the create_app factory function from the app_factory module
from .app_factory import create_app

# Create the Flask application instance us
app = create_app()

# Set the secret key for the Flask application (consider using an environment variable for security)
app.secret_key = 'your-secret'  # Replace with an environment variable

# Import the routes module to register the routes with the application
from . import routes


