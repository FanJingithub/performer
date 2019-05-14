# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os
import tornado.web
from tornado import netutil, process, httpserver
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

import MySQLdb

import json

from handlers.baseHandler import baseHandler
from handlers.labHandler import labHandler
from handlers.api_baseHandler import api_baseHandler
from handlers.api_labHandler import api_labHandler

class Application(tornado.web.Application):

    def __init__(self):

        handlers =  [
                        ("/base",      baseHandler),
                        ("/lab",      labHandler),
                        ("/api/base",      api_baseHandler),
                        ("/api/lab",      api_labHandler)
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6002)
    IOLoop.current().start()
