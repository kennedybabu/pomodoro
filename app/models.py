from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(255))
    session = db.relationship('Session', backref='user', lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique=True)
    work_time = db.Column(db.Integer)
    break_time = db.Column(db.Integer)
    break_activity = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Session {self.title}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
        
   
        