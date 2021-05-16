# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : flask_context_demo.py
# @Function : TODO

import flask
import time

app = flask.Flask(__name__)

def test_context():
    print(flask._app_ctx_stack._local.__storage__)
    print(flask._request_ctx_stack._local.__storage__)

    request_context = app.test_request_context()
    request_context.push()

    print(flask._app_ctx_stack._local.__storage__)
    print(flask._request_ctx_stack._local.__storage__)

@app.route('/hello')
def hello():
    a = flask.request.args.get('a')
    print(flask._app_ctx_stack._local.__storage__)
    print(flask._request_ctx_stack._local.__storage__)
    time.sleep(10)
    return "Hello World" + a

if __name__ == '__main__':
    print(flask._app_ctx_stack._local.__storage__)
    print(flask._request_ctx_stack._local.__storage__)

    app.run(host='localhost', port=10001, debug=True)