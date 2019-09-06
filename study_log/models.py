from study_log import db
from datetime import datetime

class Log(db.Model):

    __tablename__ = 'studylog'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    memo = db.Column(db.String(300))
    todo = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)