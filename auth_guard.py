from flask import session, redirect, url_for, request
from datetime import datetime


PUBLIC_ENDPOINTS = (
    'admin.login',
    'admin.logout',
)

def admin_auth_guard():
    # Some requests have no endpoint (favicon, errors)
    if not request.endpoint:
        return

    # Allow public admin routes
    if request.endpoint in PUBLIC_ENDPOINTS:
        return

    # Allow static files
    if request.endpoint.startswith('static'):
        return

    # Protect admin routes
    if request.endpoint.startswith('admin.'):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin.login'))
