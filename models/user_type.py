from extensions import db

class UserType(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(30), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())