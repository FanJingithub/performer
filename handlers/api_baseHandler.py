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
        self.cur.execute('''SELECT patient_id,name,sex,age,marriage,site,stage,surgery,radiotherapy,chemotherapy FROM base WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "name":res[1], "sex":res[2], "age":res[3], "marriage":res[4], "site":res[5], "stage":res[6], "surgery":res[7], "radiotherapy":res[8], "chemotherapy":res[9]}
        self.write(json.dumps(self.data))
