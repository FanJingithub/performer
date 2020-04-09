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
        try:
            page_index = self.get_argument("page_index", "0")
        except:
            page_index = "0"

        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,patho_diagnosis,lym_vas_invasion,tot_lymph_node,deep,pni,pos_lymph_node FROM pathology_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "patho_diagnosis":res[1], "lym_vas_invasion":res[2], "tot_lymph_node":res[3], "deep":res[4], "pni":res[5], "pos_lymph_node":res[6]}
        self.write(json.dumps(self.data))
