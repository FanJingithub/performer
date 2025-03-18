# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_clinical_stageHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-clinical_stage----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        try:
            page_index = self.get_argument("page_index", "0")
        except:
            page_index = "0"

        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'CRF',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,c_t_stage,c_n_stage,c_m_stage,final_stage FROM clinical_stage_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "c_t_stage":res[1], "c_n_stage":res[2], "c_m_stage":res[3], "final_stage":res[4]}
        self.write(json.dumps(self.data))
