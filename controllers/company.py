from flask import Blueprint, render_template, session, redirect, url_for
from helpers.sidebar import get_sidebar
from functools import wraps

company_bp = Blueprint(
    'company',
    __name__,
    url_prefix='/company'
)   

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return wrap

@company_bp.route('/company')
@login_required
def company_list():
    sidebar = get_sidebar(session['user_type_id'])
    return render_template('admin/company_add_frm.html', sidebar=sidebar)

@company_bp.route('/company_add')
@login_required
def company_add():
    sidebar = get_sidebar(session['user_type_id'])
    return render_template('admin/company_add_frm.html', sidebar=sidebar)
