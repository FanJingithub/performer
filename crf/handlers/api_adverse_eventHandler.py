# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_adverse_eventHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-adverse_event----------------------')
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
        self.cur.execute('''SELECT patient_id,adverse_type,start_time,end_time,nci_ctc,disposal,disposal_other,outcome,drug_relation FROM adverse_event_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", "", "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "adverse_type":res[1], "start_time":res[2], "end_time":res[3], "nci_ctc":res[4], "disposal":res[5], "disposal_other":res[6], "outcome":res[7], "drug_relation":res[8]}
        self.write(json.dumps(self.data))
