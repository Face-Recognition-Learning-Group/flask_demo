import flask
import flask_login


app = flask.Flask(__name__)
app.secret_key = 'demo'

class User(flask_login.UserMixin):
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

my_username = 'xcy'
my_password = 'xcy123456'
user_instance = User()
login_manager = flask_login.LoginManager(app=app)

@login_manager.user_loader
def user_loader(user_login_id):
    user_instance.id = user_login_id
    return user_instance

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    password = request.form.get('password')
    if my_username == username and my_password == password:
        user_instance.id = username
        return user_instance
    return

@app.route('/login', methods=['POST'])
def login():
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')
    print(username, password)
    if my_username == username and my_password == password:
        user_instance.id = username
        flask_login.login_user(user_instance)
        return flask.jsonify({'status': 200, 'message': "OK"})
    return flask.jsonify({'status': 400, 'message': "Not Valid"})

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect('/hello')

@app.route('/hello')
def hello():
    # a = flask.request.args.get('a')
    if hasattr(user_instance, 'id'):
        print(user_instance.id)
    return "Hello World"

@app.route('/hello2')
@flask_login.login_required
def hello2():
    a = flask.request.args.get('a')
    return "Hello World" + a

if __name__ == '__main__':
    app.run(port=10000, debug=True) # 启动Web服务器