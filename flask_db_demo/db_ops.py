# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : db_ops.py
# @Function : TODO

from app import mongo

def insert_(item):
    insert_result = mongo.db.demo.insert_one(item)
    return insert_result

def delete_(id_):
    delete_result = mongo.db.demo.delete_one({'id': id_})
    return delete_result

def query_(id_, with_id=False):
    data = mongo.db.demo.find()
    ans = {}
    for each_data in data:
        if each_data['id'] == id_:
            ans = each_data
            break
    if not with_id:
        ans.pop('_id')
    return ans

def modify_(id_, item):
    data = mongo.db.demo.find()
    ans = {}
    for each_data in data:
        if each_data['id'] == id_:
            ans = each_data
            break
    for each_key in item:
        ans[each_key] = item[each_key]
    modify_result = mongo.db.demo.save(ans)
    return modify_result
