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
from handlers.pathologyHandler import pathologyHandler
from handlers.surgeryHandler import surgeryHandler
from handlers.chemotherapyHandler import chemotherapyHandler
from handlers.radiotherapyHandler import radiotherapyHandler
from handlers.follow_upHandler import follow_upHandler
from handlers.form3Handler import form3Handler
from handlers.api_baseHandler import api_baseHandler
from handlers.api_labHandler import api_labHandler
from handlers.api_pathologyHandler import api_pathologyHandler
from handlers.api_surgeryHandler import api_surgeryHandler
from handlers.api_chemotherapyHandler import api_chemotherapyHandler
from handlers.api_radiotherapyHandler import api_radiotherapyHandler
from handlers.api_follow_upHandler import api_follow_upHandler
from handlers.api_form3Handler import api_form3Handler

class listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get list--------------------------')
        self.render("list.html")

class api_newHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get new--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id FROM base WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        result = 0
        for row in self.cur:
            result = 1
        self.data = { "patient_id": self.patient_id, "result": result }
        self.write(json.dumps(self.data))

class api_listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-list--------------------------')
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id,sex,age FROM base"
        self.cur.execute(sqls)
        patient_list = []
        for row in self.cur:
            patient_list.append({
                "patient_id": row[0],
                "sex": row[1],
                "age": row[2]
            })
        print(patient_list)
        self.write(json.dumps(patient_list))


class Application(tornado.web.Application):

    def __init__(self):

        handlers =  [
                        ("/list",      listHandler),
                        ("/api/new",      api_newHandler),
                        ("/api/list",      api_listHandler),
                        ("/base",      baseHandler),
                        ("/lab",      labHandler),
                        ("/pathology",      pathologyHandler),
                        ("/surgery",      surgeryHandler),
                        ("/chemotherapy",      chemotherapyHandler),
                        ("/radiotherapy",      radiotherapyHandler),
                        ("/follow_up",      follow_upHandler),
                        ("/form3",      form3Handler),
                        ("/api/base",      api_baseHandler),
                        ("/api/lab",      api_labHandler),
                        ("/api/pathology",      api_pathologyHandler),
                        ("/api/surgery",      api_surgeryHandler),
                        ("/api/chemotherapy",      api_chemotherapyHandler),
                        ("/api/radiotherapy",      api_radiotherapyHandler),
                        ("/api/follow_up",      api_follow_upHandler),
                        ("/api/form3",      api_form3Handler)
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6002)
    IOLoop.current().start()
