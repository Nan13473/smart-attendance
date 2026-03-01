from models import db

class teacher_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacherid = db.Column(db.Integer,unique = True,nullable = False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
