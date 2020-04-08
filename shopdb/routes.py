from shopdb import app
from flask import render_template
from shopdb.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    info = {
        'user': 'User'
    }
    return render_template('index.html', **info)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
