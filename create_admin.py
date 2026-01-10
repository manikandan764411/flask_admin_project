from app import app
from extensions import db
from models import AdminUser
from werkzeug.security import generate_password_hash

with app.app_context():
    user = AdminUser(
        username="admin",
        email="admin@example.com",
        password_hash=generate_password_hash("Admin@123"),
        is_active=True
    )

    db.session.add(user)
    db.session.commit()

    print("✅ Admin user created successfully")
