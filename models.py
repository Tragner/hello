from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/login'
db = SQLAlchemy(app)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(20))
    role = db.Column(db.String(20))
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)

    def __init__(self, company, role, start, end):
        self.company = company
        self.role = role
        self.start = start
        self.end = end

    def __repr__(self):
        return f'<Experience {self.company}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User {0}>'.format(self.email)