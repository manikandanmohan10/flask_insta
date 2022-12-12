from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from src.db import db
import uuid


class Fruits(db.Model):
    print('INSIDE FRUITS MODEL')
    __tablename__ = 'tbl_fruits'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    fake_id = db.Column(UUID(as_uuid=False), nullable=True)
    
    fruit_name = db.Column(db.String(), nullable=True)
    
    print('TABLE CREATED SUCCESSFULLY')
    