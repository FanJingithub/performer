# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class pathologyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get pathology--------------------------')

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
        self.cur.execute('''SELECT pathology FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()

        res = [self.patient_id, "", "", "", "", "", ""]

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''SELECT patient_id,patho_diagnosis,lym_vas_invasion,tot_lymph_node,deep,pni,pos_lymph_node FROM pathology WHERE patient_id='{0}' '''.format(self.patient_id))
            for row in self.cur:
                res = row

        if (exist==1 and edit=="0"):
            self.render("../html/read_pathology_page.html", patient_id=self.patient_id,  patho_diagnosis=res[1], lym_vas_invasion=res[2], tot_lymph_node=res[3], deep=res[4], pni=res[5], pos_lymph_node=res[6])
        else:
            self.render("../html/edit_pathology_page.html", patient_id=self.patient_id,  patho_diagnosis=res[1], lym_vas_invasion=res[2], tot_lymph_node=res[3], deep=res[4], pni=res[5], pos_lymph_node=res[6])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        patho_diagnosis = self.get_body_argument("patho_diagnosis") 
        lym_vas_invasion = self.get_body_argument("lym_vas_invasion") 
        tot_lymph_node = self.get_body_argument("tot_lymph_node") 
        deep = self.get_body_argument("deep") 
        pni = self.get_body_argument("pni") 
        pos_lymph_node = self.get_body_argument("pos_lymph_node") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sqls = '''REPLACE INTO pathology (patient_id, patho_diagnosis, lym_vas_invasion, tot_lymph_node, deep, pni, pos_lymph_node) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}') '''.format(self.patient_id, patho_diagnosis,lym_vas_invasion,tot_lymph_node,deep,pni,pos_lymph_node)
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET pathology=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,pathology) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()

        self.render("../html/read_pathology_page.html", patient_id=self.patient_id, patho_diagnosis=patho_diagnosis, lym_vas_invasion=lym_vas_invasion, tot_lymph_node=tot_lymph_node, deep=deep, pni=pni, pos_lymph_node=pos_lymph_node)
