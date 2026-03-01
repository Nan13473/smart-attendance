from flask_sqlalchemy import SQLAlchemy

# Single shared db instance — all models import from here
db = SQLAlchemy()
