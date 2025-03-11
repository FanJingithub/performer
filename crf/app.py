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
from handlers.physical_examHandler import physical_examHandler
from handlers.labHandler import labHandler
from handlers.special_examHandler import special_examHandler
from handlers.before_evaluateHandler import before_evaluateHandler
from handlers.after_evaluateHandler import after_evaluateHandler
from handlers.api_baseHandler import api_baseHandler
from handlers.api_physical_examHandler import api_physical_examHandler
from handlers.api_labHandler import api_labHandler
from handlers.api_special_examHandler import api_special_examHandler
from handlers.api_before_evaluateHandler import api_before_evaluateHandler
from handlers.api_after_evaluateHandler import api_after_evaluateHandler

class uploadHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Prepare Upload--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        print(self.patient_id)
        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'CRF',
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
        self.cur.execute('''SELECT base,physical_exam,lab,special_exam,before_evaluate,after_evaluate FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            physical_exam_page_status = row[1]
            lab_page_status = row[2]
            special_exam_page_status = row[3]
            before_evaluate_page_status = row[4]
            after_evaluate_page_status = row[5]
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
                    <span>体格检查</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(physical_exam_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/physical_exam?patient_id={1}&page_index={2}">体格检查_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/physical_exam?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(physical_exam_page_status)))
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
                    <span>特殊检查</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(special_exam_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/special_exam?patient_id={1}&page_index={2}">特殊检查_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/special_exam?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(special_exam_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗前评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(before_evaluate_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/before_evaluate?patient_id={1}&page_index={2}">治疗前评估_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/before_evaluate?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(before_evaluate_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗后评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(after_evaluate_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/after_evaluate?patient_id={1}&page_index={2}">治疗后评估_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/after_evaluate?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(after_evaluate_page_status)))
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
                                db     = 'CRF',
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
        self.cur.execute('''SELECT base,physical_exam,lab,special_exam,before_evaluate,after_evaluate FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            physical_exam_page_status = row[1]
            lab_page_status = row[2]
            special_exam_page_status = row[3]
            before_evaluate_page_status = row[4]
            after_evaluate_page_status = row[5]
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
                    <span>体格检查</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(physical_exam_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/physical_exam?patient_id={1}&page_index={2}">体格检查_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/physical_exam?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(physical_exam_page_status)))
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
                    <span>特殊检查</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(special_exam_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/special_exam?patient_id={1}&page_index={2}">特殊检查_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/special_exam?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(special_exam_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗前评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(before_evaluate_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/before_evaluate?patient_id={1}&page_index={2}">治疗前评估_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/before_evaluate?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(before_evaluate_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗后评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(after_evaluate_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/after_evaluate?patient_id={1}&page_index={2}">治疗后评估_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/after_evaluate?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(after_evaluate_page_status)))
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
                                db     = 'CRF',
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
        self.cur.execute('''SELECT base,physical_exam,lab,special_exam,before_evaluate,after_evaluate FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            physical_exam_page_status = row[1]
            lab_page_status = row[2]
            special_exam_page_status = row[3]
            before_evaluate_page_status = row[4]
            after_evaluate_page_status = row[5]
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
                    <span>体格检查</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(physical_exam_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/physical_exam?patient_id={1}&page_index={2}">体格检查_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/physical_exam?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(physical_exam_page_status)))
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
                    <span>特殊检查</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(special_exam_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/special_exam?patient_id={1}&page_index={2}">特殊检查_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/special_exam?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(special_exam_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗前评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(before_evaluate_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/before_evaluate?patient_id={1}&page_index={2}">治疗前评估_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/before_evaluate?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(before_evaluate_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗后评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(after_evaluate_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/after_evaluate?patient_id={1}&page_index={2}">治疗后评估_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/after_evaluate?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(after_evaluate_page_status)))
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
                                db     = 'CRF',
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
                                db     = 'CRF',
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
                "DELETE FROM physical_exam_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM physical_exam_9 WHERE patient_id='" + self.patient_id + "'" ,
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
                "DELETE FROM special_exam_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM special_exam_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM before_evaluate_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM before_evaluate_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM after_evaluate_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_9 WHERE patient_id='" + self.patient_id + "'" ]

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
                                db     = 'CRF',
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
                                db     = 'CRF',
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
                                db     = 'CRF',
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
                        ("/physical_exam",      physical_examHandler),
                        ("/lab",      labHandler),
                        ("/special_exam",      special_examHandler),
                        ("/before_evaluate",      before_evaluateHandler),
                        ("/after_evaluate",      after_evaluateHandler),
                        ("/api/base",      api_baseHandler),
                        ("/api/physical_exam",      api_physical_examHandler),
                        ("/api/lab",      api_labHandler),
                        ("/api/special_exam",      api_special_examHandler),
                        ("/api/before_evaluate",      api_before_evaluateHandler),
                        ("/api/after_evaluate",      api_after_evaluateHandler)
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6012)
    IOLoop.current().start()
