from extensions import db
from models.module import Module

class UserTypeModule(db.Model):
    __tablename__ = "user_type_modules"

    id = db.Column(db.Integer, primary_key=True)

    user_type_id = db.Column(
        db.Integer,
        db.ForeignKey("user_types.id"),
        nullable=False
    )

    module_id = db.Column(
        db.Integer,
        db.ForeignKey("modules.id"),
        nullable=False
    )

    # ✅ THIS WAS MISSING → CAUSE OF YOUR ERROR
    module = db.relationship("Module")
