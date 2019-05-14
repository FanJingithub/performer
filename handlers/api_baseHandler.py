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
        self.cur.execute('''SELECT patient_id,name,sex,stage,surgery,radiotherapy,size,age,marriage,grade,chemotherapy,site,CEA FROM base WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "name":res[1], "sex":res[2], "stage":res[3], "surgery":res[4], "radiotherapy":res[5], "size":res[6], "age":res[7], "marriage":res[8], "grade":res[9], "chemotherapy":res[10], "site":res[11], "CEA":res[12]}
        self.write(json.dumps(self.data))
