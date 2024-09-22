# Import the Flask application instance from the current package
from flask import render_template

# define the app instance
from . import app


# define the route for the home page
@app.route('/')
# defining the index function
def index():
    #returning the rendered template 'index.html'
    return render_template('index.html')


# define the route for the about page
@app.route('/about')
#defining the about function
def about():
    return render_template('about.html')


# define the route for the exam page
@app.route('/exam')
#defining the exam function
def exam():
    #returning the rendered template 'exam.html'
    return render_template('exam.html')
