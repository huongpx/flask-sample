from flask import Flask, render_template
from database import db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    

@app.route('/')
def index():
    return render_template('index.html')
