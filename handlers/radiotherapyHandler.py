# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class radiotherapyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get radiotherapy--------------------------')

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
        self.cur.execute('''SELECT radiotherapy FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()

        res = [self.patient_id, ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,radio_count FROM radiotherapy WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_radiotherapy_page.html", patient_id=self.patient_id , radio_count=res[1])
        else:
            self.render("../html/edit_radiotherapy_page.html", patient_id=self.patient_id , radio_count=res[1])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        radio_count = self.get_body_argument("radio_count") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO radiotherapy (patient_id, radio_count) VALUES ('{0}', '{1}') '''.format(self.patient_id, radio_count)
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET radiotherapy=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,radiotherapy) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()

        self.render("../html/read_radiotherapy_page.html", patient_id=self.patient_id, radio_count=radio_count)
