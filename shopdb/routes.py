from shopdb import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    info = {
        'user': 'User'
    }
    return render_template('index.html', **info)
