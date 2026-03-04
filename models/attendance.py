from models.user import db

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(100),nullable=True)
    student_name = db.Column(db.String(100), nullable=True)
    student_id = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(100), nullable=True)
    date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Boolean, nullable=True)

    
    

   