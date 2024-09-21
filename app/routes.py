# Import the Flask application instance from the current package
from .import app


# Define the route for the home page
@app.route('/index')
def index():
    return render_template('index.html')


# Define the route for the about page
@app.route('/about')
def about():
    return render_template('about.html')


# Define the route for the exam page
@app.route('/exam')
def exam():
    return render_template('exam.html')
