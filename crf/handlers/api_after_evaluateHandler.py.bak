# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_after_evaluateHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-after_evaluate----------------------')
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
        self.cur.execute('''SELECT patient_id,evaluate_date5,site5_0,site5_1,site5_2,site5_3,site5_4,method5_0,method5_1,method5_2,method5_3,method5_4,long_dist2_0,long_dist2_1,long_dist2_2,long_dist2_3,long_dist2_4,evaluate_date6,site6_0,site6_1,site6_2,site6_3,site6_4,method6_0,method6_1,method6_2,method6_3,method6_4,status6_0,status6_1,status6_2,status6_3,status6_4,is_evaluable2_0,is_evaluable2_1,is_evaluable2_2,is_evaluable2_3,is_evaluable2_4,total_result,evaluate_date4 FROM after_evaluate_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "evaluate_date5":res[1], "site5_0":res[2], "site5_1":res[3], "site5_2":res[4], "site5_3":res[5], "site5_4":res[6], "method5_0":res[7], "method5_1":res[8], "method5_2":res[9], "method5_3":res[10], "method5_4":res[11], "long_dist2_0":res[12], "long_dist2_1":res[13], "long_dist2_2":res[14], "long_dist2_3":res[15], "long_dist2_4":res[16], "evaluate_date6":res[17], "site6_0":res[18], "site6_1":res[19], "site6_2":res[20], "site6_3":res[21], "site6_4":res[22], "method6_0":res[23], "method6_1":res[24], "method6_2":res[25], "method6_3":res[26], "method6_4":res[27], "status6_0":res[28], "status6_1":res[29], "status6_2":res[30], "status6_3":res[31], "status6_4":res[32], "is_evaluable2_0":res[33], "is_evaluable2_1":res[34], "is_evaluable2_2":res[35], "is_evaluable2_3":res[36], "is_evaluable2_4":res[37], "total_result":res[38], "evaluate_date4":res[39]}
        self.write(json.dumps(self.data))
