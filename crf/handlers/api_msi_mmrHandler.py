# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_msi_mmrHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-msi_mmr----------------------')
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
        self.cur.execute('''SELECT patient_id,msi_result,mmr_result FROM msi_mmr_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "msi_result":res[1], "mmr_result":res[2]}
        self.write(json.dumps(self.data))
