from extensions import db

class UserTypeModule(db.Model):
    __tablename__ = "user_type_modules"

    id = db.Column(db.Integer, primary_key=True)

    user_type_id = db.Column(
        db.Integer,
        db.ForeignKey("user_type.id"),
        nullable=False
    )

    module_id = db.Column(
        db.Integer,
        db.ForeignKey("modules.id"),
        nullable=False
    )

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    __table_args__ = (
        db.UniqueConstraint("user_type_id", "module_id"),
    )
