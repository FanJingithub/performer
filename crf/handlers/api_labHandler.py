# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_labHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-lab----------------------')
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
        self.cur.execute('''SELECT patient_id,exam_date,name_0,name_1,name_2,name_3,name_4,result2_0,result2_1,result2_2,result2_3,result2_4,unit_0,unit_1,unit_2,unit_3,unit_4,valuable_0,valuable_1,valuable_2,valuable_3,valuable_4 FROM lab_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "exam_date":res[1], "name_0":res[2], "name_1":res[3], "name_2":res[4], "name_3":res[5], "name_4":res[6], "result2_0":res[7], "result2_1":res[8], "result2_2":res[9], "result2_3":res[10], "result2_4":res[11], "unit_0":res[12], "unit_1":res[13], "unit_2":res[14], "unit_3":res[15], "unit_4":res[16], "valuable_0":res[17], "valuable_1":res[18], "valuable_2":res[19], "valuable_3":res[20], "valuable_4":res[21]}
        self.write(json.dumps(self.data))
