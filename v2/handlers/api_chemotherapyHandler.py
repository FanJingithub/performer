# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_chemotherapyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-chemotherapy----------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''SELECT patient_id,chemo_way,chemo_way_other,last_chemo,chemo_time_0,chemo_time_1,chemo_time_2,chemo_way_0,chemo_way_1,chemo_way_2,desc_0,desc_1,desc_2 FROM chemotherapy WHERE patient_id='{0}' '''.format(self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "chemo_way":res[1], "chemo_way_other":res[2], "last_chemo":res[3], "chemo_time_0":res[4], "chemo_time_1":res[5], "chemo_time_2":res[6], "chemo_way_0":res[7], "chemo_way_1":res[8], "chemo_way_2":res[9], "desc_0":res[10], "desc_1":res[11], "desc_2":res[12]}
        self.write(json.dumps(self.data))
