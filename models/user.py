from models import db
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    studentid = db.Column(db.String(100), nullable=False, unique=True)
    pass_hash = db.Column(db.String(100), unique=True)
