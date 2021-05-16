# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : service.py
# @Function : TODO

import uuid
import db_ops

def make_item(a, b, c, with_id=False):
    item = {}
    if with_id:
        id_ = uuid.uuid1()
        item['id'] = id_
    item['a'] = a
    item['b'] = b
    item['c'] = c
    return item

def insert_(item):
    return db_ops.insert_(item)

def modify_(id_, item):
    return db_ops.modify_(id_, item)

def query_(id_, with_id=False):
    return db_ops.query_(id_, with_id=with_id)

def delete_(id_):
    return db_ops.delete_(id_)