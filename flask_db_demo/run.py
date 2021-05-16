# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : flask_mongo.py
# @Function : TODO


from app import app
from db_layer import db_layer

app.register_blueprint(db_layer)

if __name__ == '__main__':
    app.run(port=10000, debug=True)