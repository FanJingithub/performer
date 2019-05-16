# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_baseHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-base----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,name,sex,stage,surgery,radiotherapy,age,marriage,grade,chemotherapy,site FROM base WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "name":res[1], "sex":res[2], "stage":res[3], "surgery":res[4], "radiotherapy":res[5], "age":res[6], "marriage":res[7], "grade":res[8], "chemotherapy":res[9], "site":res[10]}
        self.write(json.dumps(self.data))
