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
        self.cur.execute('''SELECT patient_id,follow_up_date,is_liver_metastases_resection,liver_metastases_resection_date,liver_metastases_resection_patho,is_progress,progress_date,live_state,dead_date,last_date_before_missing FROM follow_up_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "follow_up_date":res[1], "is_liver_metastases_resection":res[2], "liver_metastases_resection_date":res[3], "liver_metastases_resection_patho":res[4], "is_progress":res[5], "progress_date":res[6], "live_state":res[7], "dead_date":res[8], "last_date_before_missing":res[9]}
        self.write(json.dumps(self.data))
