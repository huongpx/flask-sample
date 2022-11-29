from flask import Flask
from flask_migrate import Migrate

from models import db
from main import main as main_blueprint
from auth import auth as auth_blueprint

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
Migrate(app, db)

app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
