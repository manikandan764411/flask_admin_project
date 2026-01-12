from extensions import db

class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("modules.id"),
        nullable=True
    )

    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

