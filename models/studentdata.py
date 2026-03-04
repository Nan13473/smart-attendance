from models import db

class student_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(100), unique=True, nullable=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    student_id = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable = True)
