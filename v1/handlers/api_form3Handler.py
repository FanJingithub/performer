# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_form3Handler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-form3----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,xm,xb,xb_other,nl,sj_0,sj_1,sj_2,sj_3,sj_4,lx_0,lx_1,lx_2,lx_3,lx_4 FROM form3 WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "xm":res[1], "xb":res[2], "xb_other":res[3], "nl":res[4], "sj_0":res[5], "sj_1":res[6], "sj_2":res[7], "sj_3":res[8], "sj_4":res[9], "lx_0":res[10], "lx_1":res[11], "lx_2":res[12], "lx_3":res[13], "lx_4":res[14]}
        self.write(json.dumps(self.data))
