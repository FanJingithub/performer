# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class baseHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get base--------------------------')

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
        self.cur.execute('''SELECT base FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,name,sex,age,marriage,site,stage,grade,surgery,radiotherapy,chemotherapy FROM base WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_base_page.html", patient_id=self.patient_id,  name=res[1], sex=res[2], age=res[3], marriage=res[4], site=res[5], stage=res[6], grade=res[7], surgery=res[8], radiotherapy=res[9], chemotherapy=res[10])
        else:
            self.render("../html/edit_base_page.html", patient_id=self.patient_id,  name=res[1], sex=res[2], age=res[3], marriage=res[4], site=res[5], stage=res[6], grade=res[7], surgery=res[8], radiotherapy=res[9], chemotherapy=res[10])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        name = self.get_body_argument("name") 
        sex = self.get_body_argument("sex") 
        age = self.get_body_argument("age") 
        marriage = self.get_body_argument("marriage") 
        site = self.get_body_argument("site") 
        stage = self.get_body_argument("stage") 
        grade = self.get_body_argument("grade") 
        surgery = self.get_body_argument("surgery") 
        radiotherapy = self.get_body_argument("radiotherapy") 
        chemotherapy = self.get_body_argument("chemotherapy") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO base (patient_id, name, sex, age, marriage, site, stage, grade, surgery, radiotherapy, chemotherapy) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}') '''.format(self.patient_id, name,sex,age,marriage,site,stage,grade,surgery,radiotherapy,chemotherapy)
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET base=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,base) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()

        self.render("../html/read_base_page.html", patient_id=self.patient_id, name=name, sex=sex, age=age, marriage=marriage, site=site, stage=stage, grade=grade, surgery=surgery, radiotherapy=radiotherapy, chemotherapy=chemotherapy)
