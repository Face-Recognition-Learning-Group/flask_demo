import flask

app = flask.Flask(__name__)

@app.route('/hello')
def hello():
    a = flask.request.args.get('a')
    return "Hello World" + a

@app.route('/hello2')
def hello2():
    a = flask.request.args.get('a')
    return "Hello World" + a

if __name__ == '__main__':
    app.run(port=10000) # 启动Web服务器
    # gunicorn


# view_function      endpoint  --> hello()