# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class radiology_colonoscopyHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get radiology_colonoscopy--------------------------')

        try:
            edit = self.get_argument("edit", "0")
        except:
            edit = "0"
        try:
            page_index = self.get_argument("page_index", "0")
        except:
            page_index = "0"
        page_index = int(page_index)
        
        self.patient_id = self.get_argument("patient_id", "")
        exist = 0
        submitted = "0"
        page_status = "0"
        
        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'CRF',
                                charset= 'utf8')
        conn.autocommit(1)

        self.cur = conn.cursor()
        self.cur.execute('''SELECT radiology_colonoscopy FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            page_status = row[0]

        if len(page_status)>page_index:
            exist = 1
            submitted = page_status[page_index]

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", ""]

        if (submitted=="1"):
            # Get the data from the database
            self.cur.execute('''SELECT patient_id,chest_CT_result,chest_CT_result_other,abdomen_CT_result,abdomen_CT_result_other,pelvic_MRI_result,tumor_dist_from_anal,tumour_circle,tumor_length,can_pass,t_stage,n_stage FROM radiology_colonoscopy_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
            for row in self.cur:
                res = row

        if (exist==0):
            page_status = page_status + "0"
            sql = "UPDATE data_status SET radiology_colonoscopy='" + page_status + "' WHERE patient_id='" + self.patient_id + "'"
            self.cur.execute(sql)
        
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
                <a class="active" href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>影像学及肠镜</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiology_colonoscopy_page_status)):
            if i==page_index:
                active = ' class="active"'
            else:
                active = "" 
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
        

        if page_index>0:
            page_previous = "/radiology_colonoscopy?patient_id="+self.patient_id+"&page_index="+str(page_index-1)
        else:
            page_previous = "/base?patient_id="+self.patient_id
        if (submitted=="1" and edit=="0"):
            self.render("../html/read_radiology_colonoscopy_page.html", side_menu=side_menu, page_index=page_index, page_previous=page_previous, patient_id=self.patient_id,  chest_CT_result=res[1], chest_CT_result_other=res[2], abdomen_CT_result=res[3], abdomen_CT_result_other=res[4], pelvic_MRI_result=res[5], tumor_dist_from_anal=res[6], tumour_circle=res[7], tumor_length=res[8], can_pass=res[9], t_stage=res[10], n_stage=res[11])
        else:
            self.render("../html/edit_radiology_colonoscopy_page.html", side_menu=side_menu, page_index=page_index, page_previous=page_previous, patient_id=self.patient_id,  chest_CT_result=res[1], chest_CT_result_other=res[2], abdomen_CT_result=res[3], abdomen_CT_result_other=res[4], pelvic_MRI_result=res[5], tumor_dist_from_anal=res[6], tumour_circle=res[7], tumor_length=res[8], can_pass=res[9], t_stage=res[10], n_stage=res[11])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        try:
            page_index = self.get_argument("page_index", "0")
        except:
            page_index = "0"
        page_index = int(page_index)
        chest_CT_result = self.get_body_argument("chest_CT_result") 
        chest_CT_result_other = self.get_body_argument("chest_CT_result_other") 
        abdomen_CT_result = self.get_body_argument("abdomen_CT_result") 
        abdomen_CT_result_other = self.get_body_argument("abdomen_CT_result_other") 
        pelvic_MRI_result = self.get_body_argument("pelvic_MRI_result") 
        tumor_dist_from_anal = self.get_body_argument("tumor_dist_from_anal") 
        tumour_circle = self.get_body_argument("tumour_circle") 
        tumor_length = self.get_body_argument("tumor_length") 
        can_pass = self.get_body_argument("can_pass") 
        t_stage = self.get_body_argument("t_stage") 
        n_stage = self.get_body_argument("n_stage") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'CRF',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sql = '''REPLACE INTO radiology_colonoscopy_{0} (patient_id, chest_CT_result, chest_CT_result_other, abdomen_CT_result, abdomen_CT_result_other, pelvic_MRI_result, tumor_dist_from_anal, tumour_circle, tumor_length, can_pass, t_stage, n_stage) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}') '''.format(page_index, self.patient_id, chest_CT_result,chest_CT_result_other,abdomen_CT_result,abdomen_CT_result_other,pelvic_MRI_result,tumor_dist_from_anal,tumour_circle,tumor_length,can_pass,t_stage,n_stage)
        self.cur.execute(sql)

        sql = "SELECT radiology_colonoscopy FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sql)
        page_status = "0"
        for row in self.cur:
            page_status = row[0]

        page_status_new = page_status[0:page_index] + "1" + page_status[(page_index+1):len(page_status)]
        sql = "UPDATE data_status SET radiology_colonoscopy=" + page_status_new + " WHERE patient_id='" + self.patient_id + "'"

        self.cur.execute(sql)

        
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
                <a class="active" href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>影像学及肠镜</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(radiology_colonoscopy_page_status)):
            if i==page_index:
                active = ' class="active"'
            else:
                active = "" 
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
        

        self.write("finished")
