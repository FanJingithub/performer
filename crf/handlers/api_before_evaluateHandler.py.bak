# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_before_evaluateHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-before_evaluate----------------------')
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
        self.cur.execute('''SELECT patient_id,target_evaluate_date,site1_0,site1_1,site1_2,site1_3,site1_4,method1_0,method1_1,method1_2,method1_3,method1_4,long_dist_0,long_dist_1,long_dist_2,long_dist_3,long_dist_4,non_target_evaluate_date,site2_0,site2_1,site2_2,site2_3,site2_4,site2_5,method2_0,method2_1,method2_2,method2_3,method2_4,method2_5,status_0,status_1,status_2,status_3,status_4,status_5,is_evaluable_0,is_evaluable_1,is_evaluable_2,is_evaluable_3,is_evaluable_4,is_evaluable_5 FROM before_evaluate_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "target_evaluate_date":res[1], "site1_0":res[2], "site1_1":res[3], "site1_2":res[4], "site1_3":res[5], "site1_4":res[6], "method1_0":res[7], "method1_1":res[8], "method1_2":res[9], "method1_3":res[10], "method1_4":res[11], "long_dist_0":res[12], "long_dist_1":res[13], "long_dist_2":res[14], "long_dist_3":res[15], "long_dist_4":res[16], "non_target_evaluate_date":res[17], "site2_0":res[18], "site2_1":res[19], "site2_2":res[20], "site2_3":res[21], "site2_4":res[22], "site2_5":res[23], "method2_0":res[24], "method2_1":res[25], "method2_2":res[26], "method2_3":res[27], "method2_4":res[28], "method2_5":res[29], "status_0":res[30], "status_1":res[31], "status_2":res[32], "status_3":res[33], "status_4":res[34], "status_5":res[35], "is_evaluable_0":res[36], "is_evaluable_1":res[37], "is_evaluable_2":res[38], "is_evaluable_3":res[39], "is_evaluable_4":res[40], "is_evaluable_5":res[41]}
        self.write(json.dumps(self.data))
