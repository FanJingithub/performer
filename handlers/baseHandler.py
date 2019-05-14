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

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,name,sex,stage,surgery,radiotherapy,size,age,marriage,grade,chemotherapy,site,CEA FROM base WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_base_page.html", patient_id=self.patient_id , name=res[1], sex=res[2], stage=res[3], surgery=res[4], radiotherapy=res[5], size=res[6], age=res[7], marriage=res[8], grade=res[9], chemotherapy=res[10], site=res[11], CEA=res[12])
        else:
            self.render("../html/edit_base_page.html", patient_id=self.patient_id , name=res[1], sex=res[2], stage=res[3], surgery=res[4], radiotherapy=res[5], size=res[6], age=res[7], marriage=res[8], grade=res[9], chemotherapy=res[10], site=res[11], CEA=res[12])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        name = self.get_body_argument("name") 
        sex = self.get_body_argument("sex") 
        stage = self.get_body_argument("stage") 
        surgery = self.get_body_argument("surgery") 
        radiotherapy = self.get_body_argument("radiotherapy") 
        size = self.get_body_argument("size") 
        age = self.get_body_argument("age") 
        marriage = self.get_body_argument("marriage") 
        grade = self.get_body_argument("grade") 
        chemotherapy = self.get_body_argument("chemotherapy") 
        site = self.get_body_argument("site") 
        CEA = self.get_body_argument("CEA") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO base (patient_id, name, sex, stage, surgery, radiotherapy, size, age, marriage, grade, chemotherapy, site, CEA) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}') '''.format(self.patient_id, name,sex,stage,surgery,radiotherapy,size,age,marriage,grade,chemotherapy,site,CEA)
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

        self.render("../html/read_base_page.html", patient_id=self.patient_id, name=name, sex=sex, stage=stage, surgery=surgery, radiotherapy=radiotherapy, size=size, age=age, marriage=marriage, grade=grade, chemotherapy=chemotherapy, site=site, CEA=CEA)
