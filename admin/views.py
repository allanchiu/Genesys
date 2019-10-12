from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from admin.forms import LoginForm, UserDetailForm
from admin.models import User
from flask_login import login_user, logout_user, login_required, current_user
from exts import db

admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)


@admin.route('/userdelete/<mail_addr>')
@login_required
def userdelete(mail_addr=None):
    try:
        user = User.query.filter_by(Mail_Addr=mail_addr).first()
        db.session.delete(user)
        db.session.commit()
    finally:
        return redirect(url_for('admin.users'))


@admin.route('/userdetail/<mail_addr>', methods=['GET', 'POST'])
@login_required
def useredit(mail_addr=None):
    user = User.query.filter_by(Mail_Addr=mail_addr).first()

    if request.method == 'GET':
        form = UserDetailForm()
        return render_template('admin/userdetail.html', user=user, form=form)

    if request.method == 'POST':
        form = UserDetailForm(request.form)
        if form.validate():
            user.User_Name = request.form.get('last_name') + ' ' + request.form.get('first_name')
            user.Mail_Addr = request.form.get('mail_addr')
            user.First_Name = request.form.get('first_name')
            user.Last_Name = request.form.get('last_name')
            user.Mobile = request.form.get('mobile')
            if user.Password != request.form.get('password'):
                user.set_password(request.form.get('password'))
            db.session.commit()
            return render_template('admin/userdetail.html', user=user, form=form)
        else:
            flash('用户编辑失败')
            return render_template('admin/userdetail.html', user=user, form=form)


@admin.route('/userdetail/create', methods=['GET', 'POST'])
@login_required
def usercreate():
    if request.method == 'GET':
        form = UserDetailForm()
        return render_template('admin/userdetail.html', form=form)

    if request.method == 'POST':
        user = User()
        form = UserDetailForm(request.form)
        user.User_Name = request.form.get('last_name') + ' ' + request.form.get('first_name')
        user.Role_ID = 1
        user.Mail_Addr = request.form.get('mail_addr')
        user.First_Name = request.form.get('first_name')
        user.Last_Name = request.form.get('last_name')
        user.Mobile = request.form.get('mobile')
        user.set_password(request.form.get('password'))

        #邮箱地址判断是否被注册
        if User.query.filter_by(Mail_Addr=request.form.get('mail_addr')).first():
            user.Mail_Addr = ''
            user.Password = ''
            flash('添加用户失败，邮箱已经被注册')
            return render_template('admin/userdetail.html', user=user, form=form)

        #用户输入信息验证
        if form.validate():
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('admin.users'))
        else:
            user.Password = ''
            flash('添加用户失败')
            return render_template('admin/userdetail.html', user=user, form=form)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))
        else:
            form = LoginForm()
            return render_template('admin/login.html', form=form)

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            mail_addr = request.form.get('mail_addr')
            password = request.form.get('password')
            user = User.query.filter_by(Mail_Addr=mail_addr).first()
            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('admin.index'))
            else:
                flash('输入的用户名或者密码不正确')
                return render_template('admin/login.html', form=form)

        else:
            print(form.errors)
            return render_template('admin/login.html', form=form)


pass
