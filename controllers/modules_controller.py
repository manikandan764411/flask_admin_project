from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from controllers.admin_users import login_required
from models.module import Module
from functools import wraps
from helpers.sidebar import get_sidebar
from extensions import db, csrf



modules_bp = Blueprint(
    'modules',
    __name__,
    url_prefix='/admin'
)


@modules_bp.route('/module_add')
@login_required
def module_add():
    modules = Module.query.all()
    #print("MODULES =>", modules)
    sidebar = get_sidebar(session['user_type_id'])
    return render_template('admin/module_add_frm.html', sidebar=sidebar, modules=modules)
    

@modules_bp.route('/module_create')
@login_required
def module_create():
    parents = Module.query.filter(Module.parent_id == None).all()
    sidebar = get_sidebar(session['user_type_id'])
    return render_template('admin/module_create_frm.html', sidebar=sidebar, parents=parents)


@modules_bp.route('/add_module', methods=['GET', 'POST'])
@login_required
def add_module():
    if request.method == 'POST':

        if request.form.get('action') == 'submit_form':

            parent_id   = request.form.get('parent_id')
            module_name = request.form.get('module_name')
            module_url  = request.form.get('module_url')
            status      = request.form.get('activestat')

            # basic validation
            if not module_name or not module_url:
                flash('Module name and URL are required', 'danger')
                return redirect(url_for('module_create'))

            # save to DB
            module = Module(
                parent_id=parent_id if parent_id else None,
                name=module_name,
                url=module_url,
                status=status
            )

            db.session.add(module)
            db.session.commit()

            flash('Module created successfully', 'success')
            return redirect(url_for('module_list'))

    return render_template('module_create_frm.html')