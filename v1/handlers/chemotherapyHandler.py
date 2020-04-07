# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class chemotherapyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get chemotherapy--------------------------')

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
        self.cur.execute('''SELECT chemotherapy FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,chemo_way,chemo_way_other,last_chemo,chemo_time_0,chemo_time_1,chemo_time_2,chemo_way_0,chemo_way_1,chemo_way_2,desc_0,desc_1,desc_2 FROM chemotherapy WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_chemotherapy_page.html", patient_id=self.patient_id,  chemo_way=res[1], chemo_way_other=res[2], last_chemo=res[3], chemo_time_0=res[4], chemo_time_1=res[5], chemo_time_2=res[6], chemo_way_0=res[7], chemo_way_1=res[8], chemo_way_2=res[9], desc_0=res[10], desc_1=res[11], desc_2=res[12])
        else:
            self.render("../html/edit_chemotherapy_page.html", patient_id=self.patient_id,  chemo_way=res[1], chemo_way_other=res[2], last_chemo=res[3], chemo_time_0=res[4], chemo_time_1=res[5], chemo_time_2=res[6], chemo_way_0=res[7], chemo_way_1=res[8], chemo_way_2=res[9], desc_0=res[10], desc_1=res[11], desc_2=res[12])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        chemo_way = self.get_body_argument("chemo_way") 
        chemo_way_other = self.get_body_argument("chemo_way_other") 
        last_chemo = self.get_body_argument("last_chemo") 
        chemo_time_0 = self.get_body_argument("chemo_time_0") 
        chemo_time_1 = self.get_body_argument("chemo_time_1") 
        chemo_time_2 = self.get_body_argument("chemo_time_2") 
        chemo_way_0 = self.get_body_argument("chemo_way_0") 
        chemo_way_1 = self.get_body_argument("chemo_way_1") 
        chemo_way_2 = self.get_body_argument("chemo_way_2") 
        desc_0 = self.get_body_argument("desc_0") 
        desc_1 = self.get_body_argument("desc_1") 
        desc_2 = self.get_body_argument("desc_2") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO chemotherapy (patient_id, chemo_way, chemo_way_other, last_chemo, chemo_time_0, chemo_time_1, chemo_time_2, chemo_way_0, chemo_way_1, chemo_way_2, desc_0, desc_1, desc_2) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}') '''.format(self.patient_id, chemo_way,chemo_way_other,last_chemo,chemo_time_0,chemo_time_1,chemo_time_2,chemo_way_0,chemo_way_1,chemo_way_2,desc_0,desc_1,desc_2)
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET chemotherapy=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,chemotherapy) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()

        self.render("../html/read_chemotherapy_page.html", patient_id=self.patient_id, chemo_way=chemo_way, chemo_way_other=chemo_way_other, last_chemo=last_chemo, chemo_time_0=chemo_time_0, chemo_time_1=chemo_time_1, chemo_time_2=chemo_time_2, chemo_way_0=chemo_way_0, chemo_way_1=chemo_way_1, chemo_way_2=chemo_way_2, desc_0=desc_0, desc_1=desc_1, desc_2=desc_2)
