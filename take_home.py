import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_SDK_URL'),
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    admin = User(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return "It works\n"

@app.route("/health")
def health():
    return "Simple Server Working\n"

db.create_all()
app.run(host='0.0.0.0')
