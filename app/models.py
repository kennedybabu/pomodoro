from enum import unique
from . import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(255))
    session = db.Relationship('Session', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

class Session(db.Model):
    __tablename__ = 'sessions'

    title = db.Column(db.String(255), unique=True)
    work_time = db.Column(db.Integer)
    break_time = db.Column(db.Integer)
    break_activity = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Session {self.title}'
        
   
        