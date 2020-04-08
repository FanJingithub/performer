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
from handlers.api_baseHandler import api_baseHandler
from handlers.api_labHandler import api_labHandler
from handlers.api_pathologyHandler import api_pathologyHandler
from handlers.api_surgeryHandler import api_surgeryHandler
from handlers.api_chemotherapyHandler import api_chemotherapyHandler
from handlers.api_radiotherapyHandler import api_radiotherapyHandler
from handlers.api_follow_upHandler import api_follow_upHandler

class uploadHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Prepare Upload--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        print(self.patient_id)
        self.render("templates/upload.html", patient_id=self.patient_id)

    def post(self):
        print('----post------')
        self.patient_id = self.get_argument("patient_id", "")
        print(self.patient_id)

        self.render("templates/show.html", patient_id=self.patient_id)

        try:
            print("start---------upload")
            #imgfile = self.request.files.get('imgname')
            #print(type(imgfile))
            imgfile = self.request.files.get('pics')
            print(type(imgfile))
            try:
                print(os.listdir('./images/uploads/'+self.patient_id))
            except:
                os.mkdir('./images/uploads/'+self.patient_id)

            for img in imgfile:
                with open('./images/uploads/'+self.patient_id+'/'+img['filename'],'wb') as f:
                    f.write(img['body'])
                    #print(img['body'])
            print("---------upload -------done")

            # Get the patient's data status from the database
            conn = MySQLdb.connect( host   = 'localhost',
                                    user   = 'root',
                                    passwd = '1',
                                    db     = 'Test',
                                    charset= 'utf8')
            conn.autocommit(1)

            self.cur = conn.cursor()
            self.cur.execute("SELECT base FROM data_status WHERE patient_id='" + self.patient_id + "'")
            self.cur.close()

        except Exception as e:
            print(repr(e))
            print('--Failed--')

class api_picsHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------API_Pic--------------------------')
        self.patient_id = self.get_argument("patient_id", "")

        pics = []
        try:
            pics = os.listdir('./images/uploads/'+self.patient_id)
        except:
            pass
        self.write(json.dumps(pics))

class showHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Show Pic--------------------------')
        self.patient_id = self.get_argument("patient_id", "")

        self.render("templates/show.html", patient_id=self.patient_id)

class listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get list--------------------------')
        self.render("list.html")

class helloHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get hello--------------------------')
        self.render("Hello.html")

class api_newHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get new--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
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

class api_removeHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Remove--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = ["DELETE FROM data_status WHERE patient_id='" + self.patient_id + "'",
                "DELETE FROM base WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM lab WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM pathology WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM surgery WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM chemotherapy WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM radiotherapy WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM follow_up WHERE patient_id='" + self.patient_id + "'" ]

        for sql in sqls:
            self.cur.execute(sql)
        self.cur.close()

class api_listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-list--------------------------')
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id,name,sex,age FROM base"
        self.cur.execute(sqls)
        patient_list = []
        for row in self.cur:
            patient_list.append({
                "patient_id": row[0],
                "name": row[1],
                "sex": row[2],
                "age": row[3]
            })
        print(patient_list)
        self.write(json.dumps(patient_list))


class Application(tornado.web.Application):

    def __init__(self):

        handlers =  [
                        ("/list",      listHandler),
                        ("/hello",      helloHandler),
                        ("/api/new",      api_newHandler),
                        ("/api/remove",      api_removeHandler),
                        ("/api/list",      api_listHandler),
                        ("/upload",      uploadHandler),
                        ("/show",      showHandler),
                        ("/api/pics",      api_picsHandler),
        ("/base",      baseHandler),
                        ("/lab",      labHandler),
                        ("/pathology",      pathologyHandler),
                        ("/surgery",      surgeryHandler),
                        ("/chemotherapy",      chemotherapyHandler),
                        ("/radiotherapy",      radiotherapyHandler),
                        ("/follow_up",      follow_upHandler),
                        ("/api/base",      api_baseHandler),
                        ("/api/lab",      api_labHandler),
                        ("/api/pathology",      api_pathologyHandler),
                        ("/api/surgery",      api_surgeryHandler),
                        ("/api/chemotherapy",      api_chemotherapyHandler),
                        ("/api/radiotherapy",      api_radiotherapyHandler),
                        ("/api/follow_up",      api_follow_upHandler)
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6012)
    IOLoop.current().start()
