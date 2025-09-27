# ----------------------------------------------------------------------
# Simple Flask Application: Hello-World
# ----------------------------------------------------------------------
# This file requires the 'Flask' library.
# Install it using: pip install Flask
# To run the app: python app.py
# Then, open your browser to http://127.0.0.1:5000/
# ----------------------------------------------------------------------

from flask import Flask

# Create a Flask application instance.
# The __name__ parameter helps Flask determine the root path for the application.
app = Flask(__name__)

# Define the default route (the homepage, or '/').
# When a user navigates to the root URL, the function below will be executed.
@app.route('/')
def hello_world():
    """Returns the 'Hello-World' string when accessing the root URL."""
    return 'Hello-World'

# This block ensures the application only runs if the script is executed directly
# (not imported as a module).
if __name__ == '__main__':
    # Run the application.
    # debug=True enables the debug mode, which automatically reloads the server
    # when code changes and provides a helpful debugger.
    app.run(debug=True)