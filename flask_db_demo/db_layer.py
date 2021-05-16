# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : view.py
# @Function : TODO

from app import app, exception_handler

import flask
import service

db_layer = flask.Blueprint('db_layer', __name__)

@db_layer.route('/insert')
@exception_handler
def insert():
    a = flask.request.args.get('a')
    b = flask.request.args.get('b')
    c = flask.request.args.get('c')
    item = service.make_item(a, b, c, with_id=True)
    insert_result = service.insert_(item)
    print(insert_result)
    return flask.jsonify({'status': 200})

@db_layer.route('/modify')
@exception_handler
def modify():
    id_ = flask.request.args.get('id')

    a = flask.request.args.get('a')
    b = flask.request.args.get('b')
    c = flask.request.args.get('c')
    item = service.make_item(a, b, c, with_id=False)
    item['id'] = id_
    modify_result = service.modify_(id_, item)
    print(modify_result)
    return flask.jsonify({'status': 200})

@db_layer.route('/query')
@exception_handler
def query():
    id_ = flask.request.args.get('id')
    ans = service.query_(id_, with_id=False)
    return flask.jsonify({'ans': ans, 'status': 200})

@db_layer.route('/delete')
@exception_handler
def delete_():
    id_ = flask.request.args.get('id')
    delete_result = service.delete_(id_)
    print(delete_result)
    return flask.jsonify({'status': 200})
