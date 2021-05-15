# -*- coding: utf-8 -*-
# @Author   : Ecohnoch(xcy)
# @File     : wsgi_demo.py
# @Function : TODO

from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

class myObject:
    def __call__(self, environ, start_response):
        return self.application(environ, start_response)

    def application(self, environ, start_response):
        response = Response('Hello World!', mimetype='text/plain')
        return response(environ, start_response)

if __name__ == '__main__':
    app = myObject()
    run_simple('localhost', 5010, app)