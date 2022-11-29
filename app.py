from flask import Flask, render_template

from database import init_db, db_session
from main import main as main_blueprint
from auth import auth as auth_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run()
