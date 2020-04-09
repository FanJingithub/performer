# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_radiotherapyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-radiotherapy----------------------')
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
        self.cur.execute('''SELECT patient_id,radio_count,radio_start,radio_end FROM radiotherapy_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "radio_count":res[1], "radio_start":res[2], "radio_end":res[3]}
        self.write(json.dumps(self.data))
