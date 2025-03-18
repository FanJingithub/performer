# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_radiology_colonoscopyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-radiology_colonoscopy----------------------')
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
        self.cur.execute('''SELECT patient_id,chest_CT_result,chest_CT_result_other,abdomen_CT_result,abdomen_CT_result_other,pelvic_MRI_result,tumor_dist_from_anal,tumour_circle,tumor_length,can_pass,t_stage,n_stage FROM radiology_colonoscopy_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "chest_CT_result":res[1], "chest_CT_result_other":res[2], "abdomen_CT_result":res[3], "abdomen_CT_result_other":res[4], "pelvic_MRI_result":res[5], "tumor_dist_from_anal":res[6], "tumour_circle":res[7], "tumor_length":res[8], "can_pass":res[9], "t_stage":res[10], "n_stage":res[11]}
        self.write(json.dumps(self.data))
