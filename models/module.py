from extensions import db

class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    url = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(50), nullable=True)

    parent_id = db.Column(
        db.Integer,
        db.ForeignKey("modules.id"),
        nullable=True
    )

    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # ✅ SELF RELATION (THIS IS THE FIX)
    children = db.relationship(
        "Module",
        backref=db.backref("parent", remote_side=[id])
    )