# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : app.py
# @Function : TODO

import flask
import flask_pymongo

import uuid
import traceback
from functools import wraps

app = flask.Flask(__name__)
app.config['MONGO_URI']  = 'mongodb://my_root:my_123456@localhost:27017/mongo_db?authSource=admin'

mongo = flask_pymongo.PyMongo(app) # 持久化变量

def exception_handler(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return flask.jsonify({'status': 400})
    return decorated_view