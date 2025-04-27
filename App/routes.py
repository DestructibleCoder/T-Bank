from App import app

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to start page!"