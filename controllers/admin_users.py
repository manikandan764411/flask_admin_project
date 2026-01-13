from flask import Blueprint, render_template, session, redirect, url_for
from helpers.sidebar import get_sidebar
from functools import wraps

admin_users_bp = Blueprint(
    'admin_users',
    __name__,
    url_prefix='/admin/admin_users'
)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return wrap

@admin_users_bp.route('/')
@login_required
def index():
    sidebar = get_sidebar(session['user_type_id'])
    return render_template('admin/admin_users.html', sidebar=sidebar)
