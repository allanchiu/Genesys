from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo


class LoginForm(FlaskForm):
    mail_addr = StringField(validators=[DataRequired('请输入邮箱'), Email('请输入正确的邮件地址')])
    password = PasswordField(validators=[Length(6, 20, message='请输入6到20位间的密码')])
    btn_Submit = SubmitField()


class UserDetailForm(FlaskForm):
    last_name = StringField(validators=[DataRequired('姓不能为空')])
    first_name = StringField(validators=[DataRequired('名不能为空')])
    mobile = StringField(validators=[Length(11, 11, '手机号码必须为11为数'), Regexp('^1[35789]\d{9}$', 0, '手机号码不合法')])
    mail_addr = StringField(validators=[DataRequired('邮箱不能为空'), Email('请输入正确的邮件地址')])
    password = PasswordField(validators=[Length(8, message='密码至少8位')])
    re_password = PasswordField(validators=[Length(8, message='密码至少8位'), EqualTo("password", message="输入密码不一致")])
    btn_Submit = SubmitField()


pass
