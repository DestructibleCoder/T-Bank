from flask import render_template
from App import app

@app.route('/')
@app.route('/index')
def index():
    data = {'title': 'edulog', 'name': 'Roman'}
    return render_template('index.html', data=data)