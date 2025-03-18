# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_colonoscopy_pathologyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-colonoscopy_pathology----------------------')
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
        self.cur.execute('''SELECT patient_id,first_path_diagnose_date,pathology_type,pathology_type_other,degree_of_differentiation FROM colonoscopy_pathology_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
        res = [self.patient_id, "", "", "", ""]
        for row in self.cur:
            res = row
        self.data = { "patient_id":self.patient_id, "first_path_diagnose_date":res[1], "pathology_type":res[2], "pathology_type_other":res[3], "degree_of_differentiation":res[4]}
        self.write(json.dumps(self.data))
