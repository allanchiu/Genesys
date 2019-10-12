from flask import Flask, g
from exts import db
from admin.models import User
from flask_login import LoginManager, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '20130710'

DATABASE_URI = 'mysql+pymysql://root:Sh130710@localhost/MY_Test'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db.init_app(app)

from admin.views import admin

app.register_blueprint(admin, url_prefix='/admin')

login_manager = LoginManager(app)
login_manager.login_view = 'admin.login'
login_manager.session_protection = 'strong'
login_manager.login_message = '请输入正确的用户信息'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    if current_user.is_authenticated:
        g.user = current_user.Last_Name + " " + current_user.First_Name

@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)

pass
