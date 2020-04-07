# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class form3Handler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get form3--------------------------')

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
        self.cur.execute('''SELECT form3 FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,xm,xb,xb_other,nl,sj_0,sj_1,sj_2,sj_3,sj_4,lx_0,lx_1,lx_2,lx_3,lx_4 FROM form3 WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_form3_page.html", patient_id=self.patient_id,  xm=res[1], xb=res[2], xb_other=res[3], nl=res[4], sj_0=res[5], sj_1=res[6], sj_2=res[7], sj_3=res[8], sj_4=res[9], lx_0=res[10], lx_1=res[11], lx_2=res[12], lx_3=res[13], lx_4=res[14])
        else:
            self.render("../html/edit_form3_page.html", patient_id=self.patient_id,  xm=res[1], xb=res[2], xb_other=res[3], nl=res[4], sj_0=res[5], sj_1=res[6], sj_2=res[7], sj_3=res[8], sj_4=res[9], lx_0=res[10], lx_1=res[11], lx_2=res[12], lx_3=res[13], lx_4=res[14])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        xm = self.get_body_argument("xm") 
        xb = self.get_body_argument("xb") 
        xb_other = self.get_body_argument("xb_other") 
        nl = self.get_body_argument("nl") 
        sj_0 = self.get_body_argument("sj_0") 
        sj_1 = self.get_body_argument("sj_1") 
        sj_2 = self.get_body_argument("sj_2") 
        sj_3 = self.get_body_argument("sj_3") 
        sj_4 = self.get_body_argument("sj_4") 
        lx_0 = self.get_body_argument("lx_0") 
        lx_1 = self.get_body_argument("lx_1") 
        lx_2 = self.get_body_argument("lx_2") 
        lx_3 = self.get_body_argument("lx_3") 
        lx_4 = self.get_body_argument("lx_4") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO form3 (patient_id, xm, xb, xb_other, nl, sj_0, sj_1, sj_2, sj_3, sj_4, lx_0, lx_1, lx_2, lx_3, lx_4) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}') '''.format(self.patient_id, xm,xb,xb_other,nl,sj_0,sj_1,sj_2,sj_3,sj_4,lx_0,lx_1,lx_2,lx_3,lx_4)
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET form3=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,form3) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()

        self.render("../html/read_form3_page.html", patient_id=self.patient_id, xm=xm, xb=xb, xb_other=xb_other, nl=nl, sj_0=sj_0, sj_1=sj_1, sj_2=sj_2, sj_3=sj_3, sj_4=sj_4, lx_0=lx_0, lx_1=lx_1, lx_2=lx_2, lx_3=lx_3, lx_4=lx_4)
