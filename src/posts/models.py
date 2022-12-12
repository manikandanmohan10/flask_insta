import uuid
from datetime import datetime
from src.db import db
from sqlalchemy.dialects.postgresql import UUID


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    post = db.Column(db.String(), nullable=True)
    post_type = db.Column(db.String(), nullable=True)
    captions = db.Column(db.String(), nullable=True)
    location = db.Column()
    likes_count = db.Column(db.Integer(), nullable=True)
    comments_count = db.Column(db.Integer(), nullable=True)
    liked_by = db.Column(db.String(), nullable=True)
    commented_by = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime(), nullable=False, onupdate=datetime.now())
    location = db.Column(db.String(), nullable=True)
    ip = db.Column(db.String(), nullable=True)
    device = db.Column(db.String(), nullable=True)
    
    # user = db.relationship("User")
    
    @classmethod
    def register(cls, data):
        pass