# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_treatmentHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-treatment----------------------')
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
        self.cur.execute('''SELECT patient_id,group,treat_start_time,treat_end_time,treat_count,stop_reason,progress_time,dead_time FROM treatment_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "group":res[1], "treat_start_time":res[2], "treat_end_time":res[3], "treat_count":res[4], "stop_reason":res[5], "progress_time":res[6], "dead_time":res[7]}
        self.write(json.dumps(self.data))
