from extensions import db
from datetime import datetime

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True)
    mobile_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    gst_number = db.Column(db.String(20))
    website = db.Column(db.String(150))
    logo = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
