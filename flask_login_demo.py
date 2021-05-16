import flask
import threading
import flask_login

from functools import wraps


app = flask.Flask(__name__)
app.secret_key = 'demo'

class User(flask_login.UserMixin):
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
    def is_admin(self):
        print('[user] {}'.format(self.id))
        return True

my_username = 'xcy'
my_password = 'xcy123456'
user_instance = User()
login_manager = flask_login.LoginManager(app=app)


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if flask_login.current_user.is_admin():
            return func(*args, **kwargs)
        flask.abort(403)
    return decorated_view

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
        lock = threading.RLock()
        lock.acquire()
        # 这里线程安全，要对这两行加线程锁
        user_instance.id = username
        flask_login.login_user(user_instance)
        lock.release()
        return flask.jsonify({'status': 200, 'message': "OK"})
    return flask.jsonify({'status': 400, 'message': "Not Valid"})

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect('/hello')

@app.route('/hello')
def hello():
    if hasattr(user_instance, 'id'):
        print(user_instance.id)
    if hasattr(flask_login.current_user, 'id'):
        print(flask_login.current_user.id)
    return "Hello World"

@app.route('/hello2')
@flask_login.login_required
@admin_required
def hello2():
    a = flask.request.args.get('a')
    if hasattr(user_instance, 'id'):
        print(user_instance.id)
    if hasattr(flask_login.current_user, 'id'):
        print(flask_login.current_user.id)
        print(flask_login.current_user.is_admin())
    return "Hello World" + a

if __name__ == '__main__':
    app.run(port=10000, debug=True) # 启动Web服务器