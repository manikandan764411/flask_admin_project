from flask import Flask, redirect, url_for, session
from datetime import timedelta
import mimetypes

from extensions import db, csrf
from controllers.admin_controller import admin_bp
from config import Config
from flask_migrate import Migrate
from auth_guard import admin_auth_guard
from helpers.sidebar import get_sidebar

from controllers.admin_users import admin_users_bp


# Fix MIME types for Windows
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

def create_app():
    app = Flask(
        __name__,
        static_folder='static',
        static_url_path='/static',
        template_folder='templates'
    )

    app.config.from_object(Config)
    app.secret_key = 'super-secret-key'

    # ✅ Session timeout
    app.permanent_session_lifetime = timedelta(minutes=10)

    # ✅ Init extensions (ONLY ONCE)
    db.init_app(app)
    csrf.init_app(app)

    # ✅ Migrations
    Migrate(app, db)

    # ✅ Register blueprints
    app.register_blueprint(admin_bp)

    app.register_blueprint(admin_users_bp)


    # ✅ Auth guard
    app.before_request(admin_auth_guard)
    

    return app


app = create_app()

@app.before_request
def refresh_session():
    session.modified = True

@app.route('/')
def index():
    return redirect(url_for('admin.login'))


if __name__ == '__main__':
    app.run(debug=True)
