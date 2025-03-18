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
from handlers.radiology_colonoscopyHandler import radiology_colonoscopyHandler
from handlers.colonoscopy_pathologyHandler import colonoscopy_pathologyHandler
from handlers.msi_mmrHandler import msi_mmrHandler
from handlers.geneHandler import geneHandler
from handlers.clinical_stageHandler import clinical_stageHandler
from handlers.before_evaluateHandler import before_evaluateHandler
from handlers.treatmentHandler import treatmentHandler
from handlers.after_evaluateHandler import after_evaluateHandler
from handlers.adverse_eventHandler import adverse_eventHandler
from handlers.concomitant_medicationHandler import concomitant_medicationHandler
from handlers.follow_upHandler import follow_upHandler
from handlers.api_baseHandler import api_baseHandler
from handlers.api_physical_examHandler import api_physical_examHandler
from handlers.api_labHandler import api_labHandler
from handlers.api_special_examHandler import api_special_examHandler
from handlers.api_radiology_colonoscopyHandler import api_radiology_colonoscopyHandler
from handlers.api_colonoscopy_pathologyHandler import api_colonoscopy_pathologyHandler
from handlers.api_msi_mmrHandler import api_msi_mmrHandler
from handlers.api_geneHandler import api_geneHandler
from handlers.api_clinical_stageHandler import api_clinical_stageHandler
from handlers.api_before_evaluateHandler import api_before_evaluateHandler
from handlers.api_treatmentHandler import api_treatmentHandler
from handlers.api_after_evaluateHandler import api_after_evaluateHandler
from handlers.api_adverse_eventHandler import api_adverse_eventHandler
from handlers.api_concomitant_medicationHandler import api_concomitant_medicationHandler
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
        self.cur.execute('''SELECT base,physical_exam,lab,special_exam,radiology_colonoscopy,colonoscopy_pathology,msi_mmr,gene,clinical_stage,before_evaluate,treatment,after_evaluate,adverse_event,concomitant_medication,follow_up FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            physical_exam_page_status = row[1]
            lab_page_status = row[2]
            special_exam_page_status = row[3]
            radiology_colonoscopy_page_status = row[4]
            colonoscopy_pathology_page_status = row[5]
            msi_mmr_page_status = row[6]
            gene_page_status = row[7]
            clinical_stage_page_status = row[8]
            before_evaluate_page_status = row[9]
            treatment_page_status = row[10]
            after_evaluate_page_status = row[11]
            adverse_event_page_status = row[12]
            concomitant_medication_page_status = row[13]
            follow_up_page_status = row[14]
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
                    <span>影像学及肠镜</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiology_colonoscopy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/radiology_colonoscopy?patient_id={1}&page_index={2}">影像学及肠镜_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/radiology_colonoscopy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(radiology_colonoscopy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>肠镜病理检查结果</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(colonoscopy_pathology_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/colonoscopy_pathology?patient_id={1}&page_index={2}">肠镜病理检查结果_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/colonoscopy_pathology?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(colonoscopy_pathology_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>MSI/MMR状态</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(msi_mmr_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/msi_mmr?patient_id={1}&page_index={2}">MSI/MMR状态_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/msi_mmr?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(msi_mmr_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>基因检测</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(gene_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/gene?patient_id={1}&page_index={2}">基因检测_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/gene?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(gene_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>临床分期</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(clinical_stage_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/clinical_stage?patient_id={1}&page_index={2}">临床分期_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/clinical_stage?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(clinical_stage_page_status)))
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
                    <span>治疗</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(treatment_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/treatment?patient_id={1}&page_index={2}">治疗_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/treatment?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(treatment_page_status)))
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
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>不良事件评价</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(adverse_event_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/adverse_event?patient_id={1}&page_index={2}">不良事件评价_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/adverse_event?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(adverse_event_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>伴随用药记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(concomitant_medication_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/concomitant_medication?patient_id={1}&page_index={2}">伴随用药记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/concomitant_medication?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(concomitant_medication_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>随访评价</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(follow_up_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/follow_up?patient_id={1}&page_index={2}">随访评价_{3}</a></li>
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
        self.cur.execute('''SELECT base,physical_exam,lab,special_exam,radiology_colonoscopy,colonoscopy_pathology,msi_mmr,gene,clinical_stage,before_evaluate,treatment,after_evaluate,adverse_event,concomitant_medication,follow_up FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            physical_exam_page_status = row[1]
            lab_page_status = row[2]
            special_exam_page_status = row[3]
            radiology_colonoscopy_page_status = row[4]
            colonoscopy_pathology_page_status = row[5]
            msi_mmr_page_status = row[6]
            gene_page_status = row[7]
            clinical_stage_page_status = row[8]
            before_evaluate_page_status = row[9]
            treatment_page_status = row[10]
            after_evaluate_page_status = row[11]
            adverse_event_page_status = row[12]
            concomitant_medication_page_status = row[13]
            follow_up_page_status = row[14]
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
                    <span>影像学及肠镜</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiology_colonoscopy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/radiology_colonoscopy?patient_id={1}&page_index={2}">影像学及肠镜_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/radiology_colonoscopy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(radiology_colonoscopy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>肠镜病理检查结果</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(colonoscopy_pathology_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/colonoscopy_pathology?patient_id={1}&page_index={2}">肠镜病理检查结果_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/colonoscopy_pathology?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(colonoscopy_pathology_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>MSI/MMR状态</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(msi_mmr_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/msi_mmr?patient_id={1}&page_index={2}">MSI/MMR状态_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/msi_mmr?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(msi_mmr_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>基因检测</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(gene_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/gene?patient_id={1}&page_index={2}">基因检测_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/gene?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(gene_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>临床分期</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(clinical_stage_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/clinical_stage?patient_id={1}&page_index={2}">临床分期_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/clinical_stage?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(clinical_stage_page_status)))
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
                    <span>治疗</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(treatment_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/treatment?patient_id={1}&page_index={2}">治疗_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/treatment?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(treatment_page_status)))
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
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>不良事件评价</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(adverse_event_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/adverse_event?patient_id={1}&page_index={2}">不良事件评价_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/adverse_event?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(adverse_event_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>伴随用药记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(concomitant_medication_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/concomitant_medication?patient_id={1}&page_index={2}">伴随用药记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/concomitant_medication?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(concomitant_medication_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>随访评价</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(follow_up_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/follow_up?patient_id={1}&page_index={2}">随访评价_{3}</a></li>
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
        self.cur.execute('''SELECT base,physical_exam,lab,special_exam,radiology_colonoscopy,colonoscopy_pathology,msi_mmr,gene,clinical_stage,before_evaluate,treatment,after_evaluate,adverse_event,concomitant_medication,follow_up FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            base_page_status = row[0]
            physical_exam_page_status = row[1]
            lab_page_status = row[2]
            special_exam_page_status = row[3]
            radiology_colonoscopy_page_status = row[4]
            colonoscopy_pathology_page_status = row[5]
            msi_mmr_page_status = row[6]
            gene_page_status = row[7]
            clinical_stage_page_status = row[8]
            before_evaluate_page_status = row[9]
            treatment_page_status = row[10]
            after_evaluate_page_status = row[11]
            adverse_event_page_status = row[12]
            concomitant_medication_page_status = row[13]
            follow_up_page_status = row[14]
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
                    <span>影像学及肠镜</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiology_colonoscopy_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/radiology_colonoscopy?patient_id={1}&page_index={2}">影像学及肠镜_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/radiology_colonoscopy?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(radiology_colonoscopy_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>肠镜病理检查结果</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(colonoscopy_pathology_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/colonoscopy_pathology?patient_id={1}&page_index={2}">肠镜病理检查结果_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/colonoscopy_pathology?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(colonoscopy_pathology_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>MSI/MMR状态</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(msi_mmr_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/msi_mmr?patient_id={1}&page_index={2}">MSI/MMR状态_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/msi_mmr?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(msi_mmr_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>基因检测</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(gene_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/gene?patient_id={1}&page_index={2}">基因检测_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/gene?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(gene_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>临床分期</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(clinical_stage_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/clinical_stage?patient_id={1}&page_index={2}">临床分期_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/clinical_stage?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(clinical_stage_page_status)))
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
                    <span>治疗</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(treatment_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/treatment?patient_id={1}&page_index={2}">治疗_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/treatment?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(treatment_page_status)))
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
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>不良事件评价</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(adverse_event_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/adverse_event?patient_id={1}&page_index={2}">不良事件评价_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/adverse_event?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(adverse_event_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>伴随用药记录</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(concomitant_medication_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/concomitant_medication?patient_id={1}&page_index={2}">伴随用药记录_{3}</a></li>
            '''.format(active,self.patient_id,str(i),str(i+1))
        side_menu = side_menu + '''
                <li><a  href="/concomitant_medication?patient_id={0}&page_index={1}">新增</a></li>
            '''.format(self.patient_id,str(len(concomitant_medication_page_status)))
        side_menu = side_menu + '''
                </ul>
            </li>
            '''
        
        side_menu = side_menu + '''
            <li class="sub-menu">
                <a href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>随访评价</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(follow_up_page_status)):
            side_menu = side_menu + '''
                <li{0}><a  href="/follow_up?patient_id={1}&page_index={2}">随访评价_{3}</a></li>
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
                "DELETE FROM radiology_colonoscopy_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM radiology_colonoscopy_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM colonoscopy_pathology_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM colonoscopy_pathology_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM msi_mmr_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM msi_mmr_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM gene_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM gene_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM clinical_stage_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM clinical_stage_9 WHERE patient_id='" + self.patient_id + "'" ,
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
                "DELETE FROM treatment_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM treatment_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM after_evaluate_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM after_evaluate_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM adverse_event_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM adverse_event_9 WHERE patient_id='" + self.patient_id + "'" ,
                "DELETE FROM concomitant_medication_0 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_1 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_2 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_3 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_4 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_5 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_6 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_7 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_8 WHERE patient_id='" + self.patient_id + "'" 
                "DELETE FROM concomitant_medication_9 WHERE patient_id='" + self.patient_id + "'" ,
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
                        ("/radiology_colonoscopy",      radiology_colonoscopyHandler),
                        ("/colonoscopy_pathology",      colonoscopy_pathologyHandler),
                        ("/msi_mmr",      msi_mmrHandler),
                        ("/gene",      geneHandler),
                        ("/clinical_stage",      clinical_stageHandler),
                        ("/before_evaluate",      before_evaluateHandler),
                        ("/treatment",      treatmentHandler),
                        ("/after_evaluate",      after_evaluateHandler),
                        ("/adverse_event",      adverse_eventHandler),
                        ("/concomitant_medication",      concomitant_medicationHandler),
                        ("/follow_up",      follow_upHandler),
                        ("/api/base",      api_baseHandler),
                        ("/api/physical_exam",      api_physical_examHandler),
                        ("/api/lab",      api_labHandler),
                        ("/api/special_exam",      api_special_examHandler),
                        ("/api/radiology_colonoscopy",      api_radiology_colonoscopyHandler),
                        ("/api/colonoscopy_pathology",      api_colonoscopy_pathologyHandler),
                        ("/api/msi_mmr",      api_msi_mmrHandler),
                        ("/api/gene",      api_geneHandler),
                        ("/api/clinical_stage",      api_clinical_stageHandler),
                        ("/api/before_evaluate",      api_before_evaluateHandler),
                        ("/api/treatment",      api_treatmentHandler),
                        ("/api/after_evaluate",      api_after_evaluateHandler),
                        ("/api/adverse_event",      api_adverse_eventHandler),
                        ("/api/concomitant_medication",      api_concomitant_medicationHandler),
                        ("/api/follow_up",      api_follow_upHandler)
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6012)
    IOLoop.current().start()
