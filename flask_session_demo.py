import flask

app = flask.Flask(__name__)
app.secret_key = 'xxx'

@app.route('/set_session')
def hello():
    user = 'xxx'
    flask.session['user'] = user
    return user

@app.route('/get_session')
def hello2():
    a = flask.session['user']
    return a

if __name__ == '__main__':
    app.run(port=10001, debug=True)