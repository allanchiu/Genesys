from exts import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'USER'

    id = db.Column(db.Integer, primary_key=True)
    User_Name = db.Column(db.String(20))
    Role_ID = db.Column(db.Integer)
    Mail_Addr = db.Column(db.String(30))
    Password = db.Column(db.String(20))
    First_Name = db.Column(db.String(20))
    Last_Name = db.Column(db.String(20))
    Mobile = db.Column(db.String(11))

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)


pass
