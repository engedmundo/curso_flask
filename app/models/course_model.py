from app import db


class Course(db.Model):
    __table_name__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date, nullable=True)
