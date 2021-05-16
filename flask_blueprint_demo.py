# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : flask_blueprint_demo.py
# @Function : TODO

import flask

app = flask.Flask(__name__)
demo_print = flask.Blueprint('demo', __name__)

@demo_print.route('/demo')
def demo():
    return "demo"

# app.register_blueprint(demo_print)
if __name__ == '__main__':
    app.run(port=10002, debug=True)