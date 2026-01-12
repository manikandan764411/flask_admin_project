from extensions import db

class AdminUser(db.Model):
    __tablename__ = 'admin_users'

    id = db.Column(db.Integer, primary_key=True)

    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'), nullable=False)

    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    is_active = db.Column(db.Boolean, default=True)

    remember_token = db.Column(db.String(100))
    reset_token = db.Column(db.String(100))
    reset_token_expiry = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())



