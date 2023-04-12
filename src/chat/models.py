from src.db import db
from datetime import datetime

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sent_text = db.Column(db.String(255), nullable=True)
    received_text = db.Column(db.String(255), nullable=True)
    time = db.Column(db.DateTime(), onupdate=datetime.now())