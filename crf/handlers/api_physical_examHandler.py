# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_physical_examHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-physical_exam----------------------')
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
        self.cur.execute('''SELECT patient_id,physical_exam_1,physical_exam_1_other,annal_dist,manxing,manxing_other,family_tumor,family_tumor_other,self_immune,self_immune_other FROM physical_exam_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "physical_exam_1":res[1], "physical_exam_1_other":res[2], "annal_dist":res[3], "manxing":res[4], "manxing_other":res[5], "family_tumor":res[6], "family_tumor_other":res[7], "self_immune":res[8], "self_immune_other":res[9]}
        self.write(json.dumps(self.data))
