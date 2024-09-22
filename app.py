# import the Flask application instance from the app package
from app import app

# start the Flask development server
if __name__ == '__main__':
    # start the Flask development server in debug mode
    app.run(debug=True)


