from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from models.admin_user import AdminUser
from functools import wraps



admin_bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin'
)


def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function



@admin_bp.route('/')
@admin_login_required
def home():
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
@admin_login_required
def dashboard():
    return render_template('admin/index.html')

@admin_bp.route('/register')
def demo():
    return render_template('admin/register.html')

@admin_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()   # removes all session data
    return redirect(url_for('admin.login'))


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('admin_logged_in'):
        return redirect(url_for('admin.dashboard'))
     
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = AdminUser.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session.permanent = True  # ✅ THIS IS REQUIRED
            session['admin_logged_in'] = True
            session['admin_id'] = user.id
            session['admin_username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard')) 
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('admin.dashboard'))

    return render_template('admin/login.html')

    
