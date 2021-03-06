# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_pathologyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-pathology----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,patho_diagnosis,lym_vas_invasion,tot_lymph_node,deep,pni,pos_lymph_node FROM pathology WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "patho_diagnosis":res[1], "lym_vas_invasion":res[2], "tot_lymph_node":res[3], "deep":res[4], "pni":res[5], "pos_lymph_node":res[6]}
        self.write(json.dumps(self.data))
