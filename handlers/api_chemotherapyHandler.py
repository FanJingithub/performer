# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_chemotherapyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-chemotherapy----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,chemo_way,last_chemo FROM chemotherapy WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "chemo_way":res[1], "last_chemo":res[2]}
        self.write(json.dumps(self.data))
