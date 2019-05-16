# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_follow_upHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-follow_up----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,recurrance FROM follow_up WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "recurrance":res[1]}
        self.write(json.dumps(self.data))
