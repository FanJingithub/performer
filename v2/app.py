# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os
import tornado.web
from tornado import netutil, process, httpserver
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

import MySQLdb

import json

from handlers.baseHandler import baseHandler
from handlers.labHandler import labHandler
from handlers.pathologyHandler import pathologyHandler
from handlers.surgeryHandler import surgeryHandler
from handlers.chemotherapyHandler import chemotherapyHandler
from handlers.radiotherapyHandler import radiotherapyHandler
from handlers.follow_upHandler import follow_upHandler
from handlers.api_baseHandler import api_baseHandler
from handlers.api_labHandler import api_labHandler
from handlers.api_pathologyHandler import api_pathologyHandler
from handlers.api_surgeryHandler import api_surgeryHandler
from handlers.api_chemotherapyHandler import api_chemotherapyHandler
from handlers.api_radiotherapyHandler import api_radiotherapyHandler
from handlers.api_follow_upHandler import api_follow_upHandler

class uploadHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Prepare Upload--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        print(self.patient_id)
        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        self.cur = conn.cursor()
        
        side_menu = '''
            <li class="mt">
		        <a href="/list">
                        <i class="fa fa-tasks"></i>
                        <span>病例列表</span>
                    </a>
            </li>
            '''
        self.cur.execute('''SELECT base,lab,pathology,surgery,chemotherapy,radiotherapy,follow_up FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            lab_page_status = row[1]
            pathology_page_status = row[2]
            surgery_page_status = row[3]
            chemotherapy_page_status = row[4]
            radiotherapy_page_status = row[5]
            follow_up_page_status = row[6]
        self.cur.close()
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>基本信息</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(base_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/base?patient_id={1}&page_index={2}">基本信息_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/base?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(base_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>检验报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(lab_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/lab?patient_id={1}&page_index={2}">检验报告_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/lab?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(lab_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>病理报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(pathology_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/pathology?patient_id={1}&page_index={2}">病理报告_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/pathology?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(pathology_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>手术记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(surgery_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/surgery?patient_id={1}&page_index={2}">手术记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/surgery?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(surgery_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>化疗记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(chemotherapy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/chemotherapy?patient_id={1}&page_index={2}">化疗记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/chemotherapy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(chemotherapy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>放疗记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiotherapy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/radiotherapy?patient_id={1}&page_index={2}">放疗记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/radiotherapy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(radiotherapy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>随访记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(follow_up_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/follow_up?patient_id={1}&page_index={2}">随访记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/follow_up?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(follow_up_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                    <a href="/upload?patient_id={0}">
                    <i class="fa fa-tasks"></i>
                    <span>上传图片</span>
                </a>
            </li>

            <li class="sub-menu">
                    <a href="/show?patient_id={0}">
                    <i class="fa fa-tasks"></i>
                    <span>查阅图片</span>
                </a>
            </li>
        '''.format(self.patient_id)
        
        self.render("templates/upload.html", side_menu=side_menu, patient_id=self.patient_id)

    def post(self):
        print('----post------')
        self.patient_id = self.get_argument("patient_id", "")
        print(self.patient_id)

        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)

        self.cur = conn.cursor()
        
        side_menu = '''
            <li class="mt">
		        <a href="/list">
                        <i class="fa fa-tasks"></i>
                        <span>病例列表</span>
                    </a>
            </li>
            '''
        self.cur.execute('''SELECT base,lab,pathology,surgery,chemotherapy,radiotherapy,follow_up FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            lab_page_status = row[1]
            pathology_page_status = row[2]
            surgery_page_status = row[3]
            chemotherapy_page_status = row[4]
            radiotherapy_page_status = row[5]
            follow_up_page_status = row[6]
        self.cur.close()
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>基本信息</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(base_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/base?patient_id={1}&page_index={2}">基本信息_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/base?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(base_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>检验报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(lab_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/lab?patient_id={1}&page_index={2}">检验报告_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/lab?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(lab_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>病理报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(pathology_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/pathology?patient_id={1}&page_index={2}">病理报告_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/pathology?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(pathology_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>手术记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(surgery_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/surgery?patient_id={1}&page_index={2}">手术记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/surgery?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(surgery_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>化疗记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(chemotherapy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/chemotherapy?patient_id={1}&page_index={2}">化疗记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/chemotherapy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(chemotherapy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>放疗记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiotherapy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/radiotherapy?patient_id={1}&page_index={2}">放疗记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/radiotherapy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(radiotherapy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>随访记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(follow_up_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/follow_up?patient_id={1}&page_index={2}">随访记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/follow_up?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(follow_up_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                    <a href="/upload?patient_id={0}">
                    <i class="fa fa-tasks"></i>
                    <span>上传图片</span>
                </a>
            </li>

            <li class="sub-menu">
                    <a href="/show?patient_id={0}">
                    <i class="fa fa-tasks"></i>
                    <span>查阅图片</span>
                </a>
            </li>
        '''.format(self.patient_id)
        
        self.render("templates/show.html", side_menu=side_menu, patient_id=self.patient_id)

        try:
            print("start---------upload")
            #imgfile = self.request.files.get('imgname')
            #print(type(imgfile))
            imgfile = self.request.files.get('pics')
            print(type(imgfile))
            try:
                print(os.listdir('./images/uploads/'+self.patient_id))
            except:
                os.mkdir('./images/uploads/'+self.patient_id)

            for img in imgfile:
                with open('./images/uploads/'+self.patient_id+'/'+img['filename'],'wb') as f:
                    f.write(img['body'])
                    #print(img['body'])
            print("---------upload -------done")

            self.cur.execute("SELECT base FROM data_status WHERE patient_id='" + self.patient_id + "'")
            self.cur.close()

        except Exception as e:
            print(repr(e))
            print('--Failed--')

class api_picsHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------API_Pic--------------------------')
        self.patient_id = self.get_argument("patient_id", "")

        pics = []
        try:
            pics = os.listdir('./images/uploads/'+self.patient_id)
        except:
            pass
        self.write(json.dumps(pics))

class showHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Show Pic--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        self.cur = conn.cursor()
        
        side_menu = '''
            <li class="mt">
		        <a href="/list">
                        <i class="fa fa-tasks"></i>
                        <span>病例列表</span>
                    </a>
            </li>
            '''
        self.cur.execute('''SELECT base,lab,pathology,surgery,chemotherapy,radiotherapy,follow_up FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            lab_page_status = row[1]
            pathology_page_status = row[2]
            surgery_page_status = row[3]
            chemotherapy_page_status = row[4]
            radiotherapy_page_status = row[5]
            follow_up_page_status = row[6]
        self.cur.close()
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>基本信息</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(base_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/base?patient_id={1}&page_index={2}">基本信息_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/base?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(base_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>检验报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(lab_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/lab?patient_id={1}&page_index={2}">检验报告_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/lab?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(lab_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>病理报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(pathology_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/pathology?patient_id={1}&page_index={2}">病理报告_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/pathology?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(pathology_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>手术记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(surgery_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/surgery?patient_id={1}&page_index={2}">手术记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/surgery?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(surgery_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>化疗记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(chemotherapy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/chemotherapy?patient_id={1}&page_index={2}">化疗记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/chemotherapy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(chemotherapy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>放疗记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiotherapy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/radiotherapy?patient_id={1}&page_index={2}">放疗记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/radiotherapy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(radiotherapy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>随访记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(follow_up_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/follow_up?patient_id={1}&page_index={2}">随访记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/follow_up?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(follow_up_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                    <a href="/upload?patient_id={0}">
                    <i class="fa fa-tasks"></i>
                    <span>上传图片</span>
                </a>
            </li>

            <li class="sub-menu">
                    <a href="/show?patient_id={0}">
                    <i class="fa fa-tasks"></i>
                    <span>查阅图片</span>
                </a>
            </li>
        '''.format(self.patient_id)
        
        self.render("templates/show.html", side_menu=side_menu, patient_id=self.patient_id)

class listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get list--------------------------')
        self.render("list.html")

class helloHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get hello--------------------------')
        self.render("Hello.html")

class api_newHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get new--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id FROM base_0 WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        result = 0
        for row in self.cur:
            result = 1
        if (result == 0):
            sql = "INSERT INTO data_status (patient_id,base) VALUES ('" + self.patient_id + "','0')"
            self.cur.execute(sql)
        self.cur.close()
        self.data = { "patient_id": self.patient_id, "result": result }
        self.write(json.dumps(self.data))

class api_removeHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Remove--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = ["DELETE FROM data_status WHERE patient_id='" + self.patient_id + "'",
                "DELETE FROM base_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM base_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM lab_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM lab_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM pathology_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM pathology_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM surgery_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM surgery_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM chemotherapy_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM chemotherapy_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM radiotherapy_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiotherapy_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM follow_up_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM follow_up_9 WHERE patient_id='" + self.patient_id + "'" ]

        for sql in sqls:
            self.cur.execute(sql)
        self.cur.close()

class api_removePageHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------remove page--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        self.page_name = self.get_argument("page_name", "")
        self.page_index = self.get_argument("page_index", "")
        page_index =int(self.page_index)
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sql = "SELECT " + self.page_name + " FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sql)
        page_status = "0"
        for row in self.cur:
            page_status = row[0]
        if page_index>0:
            page_status_new = page_status[0:page_index] + page_status[(page_index+1):len(page_status)]
        else:
            page_status_new = "0"
        sql = "UPDATE data_status SET " + self.page_name + "=" + page_status_new + " WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sql)

        sql = "DELETE FROM " + self.page_name + "_" + str(page_index)+ " WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sql)

        for i in range(page_index,len(page_status)-1):
            sql = "INSERT INTO " + self.page_name + "_" + str(i)+ " SELECT * FROM " + self.page_name + "_" + str(i+1) + " WHERE patient_id='" + self.patient_id + "'"
            self.cur.execute(sql)
            sql = "DELETE FROM " + self.page_name + "_" + str(i+1)+ " WHERE patient_id='" + self.patient_id + "'"
            self.cur.execute(sql)
        self.cur.close()
        self.write("finished")

class downloadExcelHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------download Excel--------------------------')
        os.system("python3 download_xls.py")
        self.set_header ('Content-Disposition', 'attachment; filename='+"data.xls")
        with open("download/data.xls", 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.write(data)
        self.finish()

class indexHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------index--------------------------')
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        cur = conn.cursor()
        sql = "SELECT patient_id FROM data_status"
        cur.execute(sql)
        num_plan = 50
        num_tot = 0
        for row in cur:
            num_tot = num_tot + 1
        percent_0 = int(num_tot/num_plan*100)
        percent_1 = 100-percent_0
        if num_tot==0:
            num = [0,0,0,0,0,0]
        if num_tot==1:
            num = [0,0,0,0,0,1]
        if num_tot==2:
            num = [0,0,0,0,1,1]
        if num_tot==3:
            num = [0,0,0,1,0,2]
        if num_tot==4:
            num = [0,0,0,1,0,3]
        if num_tot>4:
            num = [int(num_tot*0.15),int(num_tot*0.15),int(num_tot*0.15),int(num_tot*0.15),int(num_tot*0.15)]
            num_6 = num_tot - (num[0]+num[1]+num[2]+num[3]+num[4])
            num.extend([num_6])
        
        self.render("templates/index.html", num_tot=num_tot, percent_0=percent_0, percent_1=percent_1, num_1=num[0], num_2=num[1], num_3=num[2], num_4=num[3], num_5=num[4], num_6=num[5])

class api_listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-list--------------------------')
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'Test',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id,name,sex,age FROM base_0"
        self.cur.execute(sqls)
        patient_list = []
        for row in self.cur:
            patient_list.append({
                "patient_id": row[0],
                "name": row[1],
                "sex": row[2],
                "age": row[3]
            })
        print(patient_list)
        self.write(json.dumps(patient_list))


class Application(tornado.web.Application):

    def __init__(self):

        handlers =  [
                        ("/list",      listHandler),
                        ("/hello",      helloHandler),
                        ("/index",      indexHandler),
                        ("/api/new",      api_newHandler),
                        ("/api/remove",      api_removeHandler),
                        ("/api/removePage",      api_removePageHandler),
                        ("/downloadExcel",      downloadExcelHandler),
                        ("/api/list",      api_listHandler),
                        ("/upload",      uploadHandler),
                        ("/show",      showHandler),
                        ("/api/pics",      api_picsHandler),
        ("/base",      baseHandler),
                        ("/lab",      labHandler),
                        ("/pathology",      pathologyHandler),
                        ("/surgery",      surgeryHandler),
                        ("/chemotherapy",      chemotherapyHandler),
                        ("/radiotherapy",      radiotherapyHandler),
                        ("/follow_up",      follow_upHandler),
                        ("/api/base",      api_baseHandler),
                        ("/api/lab",      api_labHandler),
                        ("/api/pathology",      api_pathologyHandler),
                        ("/api/surgery",      api_surgeryHandler),
                        ("/api/chemotherapy",      api_chemotherapyHandler),
                        ("/api/radiotherapy",      api_radiotherapyHandler),
                        ("/api/follow_up",      api_follow_upHandler)
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6012)
    IOLoop.current().start()
