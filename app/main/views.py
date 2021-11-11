from flask import render_template, request, redirect, url_for
from . import main
from ..models import User
from flask_login import login_required

@main.route('/')
def index():
    '''
    View root function that returns the index page and its data
    '''
    title = 'Welcome, pomodoro'
    return render_template('index.html', title = title)


@main.route('/session/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_session(id):
    pass

