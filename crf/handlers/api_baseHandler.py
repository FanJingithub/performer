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
        self.cur.execute('''SELECT patient_id,name,sex,age,first_consult_date,birth_date,rt_num,patient_num,height,weight,tibiao_area,kps,ECOG FROM base_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "name":res[1], "sex":res[2], "age":res[3], "first_consult_date":res[4], "birth_date":res[5], "rt_num":res[6], "patient_num":res[7], "height":res[8], "weight":res[9], "tibiao_area":res[10], "kps":res[11], "ECOG":res[12]}
        self.write(json.dumps(self.data))
