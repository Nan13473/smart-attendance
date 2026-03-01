from models import db

class student_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(100), unique=True, nullable=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable = True)
    attendance = db.Column(db.Integer, nullable=False)
