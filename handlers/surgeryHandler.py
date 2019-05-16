# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class surgeryHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get surgery--------------------------')

        try:
            edit = self.get_argument("edit", "0")
        except:
            edit = "0"
        
        self.patient_id = self.get_argument("patient_id", "")
        exist = 0
        
        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        self.cur = conn.cursor()
        self.cur.execute('''SELECT surgery FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()

        res = [self.patient_id, ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,resection_way FROM surgery WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_surgery_page.html", patient_id=self.patient_id , resection_way=res[1])
        else:
            self.render("../html/edit_surgery_page.html", patient_id=self.patient_id , resection_way=res[1])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        resection_way = self.get_body_argument("resection_way") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO surgery (patient_id, resection_way) VALUES ('{0}', '{1}') '''.format(self.patient_id, resection_way)
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET surgery=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,surgery) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()

        self.render("../html/read_surgery_page.html", patient_id=self.patient_id, resection_way=resection_way)
