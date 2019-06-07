#hrms project

from flask import Flask

app = Flask(__name__, template_folder='template', static_folder='static')

from hrms import app
if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=True)