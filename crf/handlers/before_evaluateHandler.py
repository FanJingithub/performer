# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class before_evaluateHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get before_evaluate--------------------------')

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
        self.cur.execute('''SELECT before_evaluate FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            page_status = row[0]

        if len(page_status)>page_index:
            exist = 1
            submitted = page_status[page_index]

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        if (submitted=="1"):
            # Get the data from the database
            self.cur.execute('''SELECT patient_id,target_evaluate_date,site1_0,site1_1,site1_2,site1_3,site1_4,method1_0,method1_1,method1_2,method1_3,method1_4,long_dist_0,long_dist_1,long_dist_2,long_dist_3,long_dist_4,non_target_evaluate_date,site2_0,site2_1,site2_2,site2_3,site2_4,site2_5,method2_0,method2_1,method2_2,method2_3,method2_4,method2_5,status_0,status_1,status_2,status_3,status_4,status_5,is_evaluable_0,is_evaluable_1,is_evaluable_2,is_evaluable_3,is_evaluable_4,is_evaluable_5 FROM before_evaluate_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
            for row in self.cur:
                res = row

        if (exist==0):
            page_status = page_status + "0"
            sql = "UPDATE data_status SET before_evaluate='" + page_status + "' WHERE patient_id='" + self.patient_id + "'"
            self.cur.execute(sql)
        
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
                <a class="active" href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗前评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(before_evaluate_page_status)):
            if i==page_index:
                active = ' class="active"'
            else:
                active = "" 
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
        

        if page_index>0:
            page_previous = "/before_evaluate?patient_id="+self.patient_id+"&page_index="+str(page_index-1)
        else:
            page_previous = "/base?patient_id="+self.patient_id
        if (submitted=="1" and edit=="0"):
            self.render("../html/read_before_evaluate_page.html", side_menu=side_menu, page_index=page_index, page_previous=page_previous, patient_id=self.patient_id,  target_evaluate_date=res[1], site1_0=res[2], site1_1=res[3], site1_2=res[4], site1_3=res[5], site1_4=res[6], method1_0=res[7], method1_1=res[8], method1_2=res[9], method1_3=res[10], method1_4=res[11], long_dist_0=res[12], long_dist_1=res[13], long_dist_2=res[14], long_dist_3=res[15], long_dist_4=res[16], non_target_evaluate_date=res[17], site2_0=res[18], site2_1=res[19], site2_2=res[20], site2_3=res[21], site2_4=res[22], site2_5=res[23], method2_0=res[24], method2_1=res[25], method2_2=res[26], method2_3=res[27], method2_4=res[28], method2_5=res[29], status_0=res[30], status_1=res[31], status_2=res[32], status_3=res[33], status_4=res[34], status_5=res[35], is_evaluable_0=res[36], is_evaluable_1=res[37], is_evaluable_2=res[38], is_evaluable_3=res[39], is_evaluable_4=res[40], is_evaluable_5=res[41])
        else:
            self.render("../html/edit_before_evaluate_page.html", side_menu=side_menu, page_index=page_index, page_previous=page_previous, patient_id=self.patient_id,  target_evaluate_date=res[1], site1_0=res[2], site1_1=res[3], site1_2=res[4], site1_3=res[5], site1_4=res[6], method1_0=res[7], method1_1=res[8], method1_2=res[9], method1_3=res[10], method1_4=res[11], long_dist_0=res[12], long_dist_1=res[13], long_dist_2=res[14], long_dist_3=res[15], long_dist_4=res[16], non_target_evaluate_date=res[17], site2_0=res[18], site2_1=res[19], site2_2=res[20], site2_3=res[21], site2_4=res[22], site2_5=res[23], method2_0=res[24], method2_1=res[25], method2_2=res[26], method2_3=res[27], method2_4=res[28], method2_5=res[29], status_0=res[30], status_1=res[31], status_2=res[32], status_3=res[33], status_4=res[34], status_5=res[35], is_evaluable_0=res[36], is_evaluable_1=res[37], is_evaluable_2=res[38], is_evaluable_3=res[39], is_evaluable_4=res[40], is_evaluable_5=res[41])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        try:
            page_index = self.get_argument("page_index", "0")
        except:
            page_index = "0"
        page_index = int(page_index)
        target_evaluate_date = self.get_body_argument("target_evaluate_date") 
        site1_0 = self.get_body_argument("site1_0") 
        site1_1 = self.get_body_argument("site1_1") 
        site1_2 = self.get_body_argument("site1_2") 
        site1_3 = self.get_body_argument("site1_3") 
        site1_4 = self.get_body_argument("site1_4") 
        method1_0 = self.get_body_argument("method1_0") 
        method1_1 = self.get_body_argument("method1_1") 
        method1_2 = self.get_body_argument("method1_2") 
        method1_3 = self.get_body_argument("method1_3") 
        method1_4 = self.get_body_argument("method1_4") 
        long_dist_0 = self.get_body_argument("long_dist_0") 
        long_dist_1 = self.get_body_argument("long_dist_1") 
        long_dist_2 = self.get_body_argument("long_dist_2") 
        long_dist_3 = self.get_body_argument("long_dist_3") 
        long_dist_4 = self.get_body_argument("long_dist_4") 
        non_target_evaluate_date = self.get_body_argument("non_target_evaluate_date") 
        site2_0 = self.get_body_argument("site2_0") 
        site2_1 = self.get_body_argument("site2_1") 
        site2_2 = self.get_body_argument("site2_2") 
        site2_3 = self.get_body_argument("site2_3") 
        site2_4 = self.get_body_argument("site2_4") 
        site2_5 = self.get_body_argument("site2_5") 
        method2_0 = self.get_body_argument("method2_0") 
        method2_1 = self.get_body_argument("method2_1") 
        method2_2 = self.get_body_argument("method2_2") 
        method2_3 = self.get_body_argument("method2_3") 
        method2_4 = self.get_body_argument("method2_4") 
        method2_5 = self.get_body_argument("method2_5") 
        status_0 = self.get_body_argument("status_0") 
        status_1 = self.get_body_argument("status_1") 
        status_2 = self.get_body_argument("status_2") 
        status_3 = self.get_body_argument("status_3") 
        status_4 = self.get_body_argument("status_4") 
        status_5 = self.get_body_argument("status_5") 
        is_evaluable_0 = self.get_body_argument("is_evaluable_0") 
        is_evaluable_1 = self.get_body_argument("is_evaluable_1") 
        is_evaluable_2 = self.get_body_argument("is_evaluable_2") 
        is_evaluable_3 = self.get_body_argument("is_evaluable_3") 
        is_evaluable_4 = self.get_body_argument("is_evaluable_4") 
        is_evaluable_5 = self.get_body_argument("is_evaluable_5") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'CRF',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sql = '''REPLACE INTO before_evaluate_{0} (patient_id, target_evaluate_date, site1_0, site1_1, site1_2, site1_3, site1_4, method1_0, method1_1, method1_2, method1_3, method1_4, long_dist_0, long_dist_1, long_dist_2, long_dist_3, long_dist_4, non_target_evaluate_date, site2_0, site2_1, site2_2, site2_3, site2_4, site2_5, method2_0, method2_1, method2_2, method2_3, method2_4, method2_5, status_0, status_1, status_2, status_3, status_4, status_5, is_evaluable_0, is_evaluable_1, is_evaluable_2, is_evaluable_3, is_evaluable_4, is_evaluable_5) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}', '{30}', '{31}', '{32}', '{33}', '{34}', '{35}', '{36}', '{37}', '{38}', '{39}', '{40}', '{41}', '{42}') '''.format(page_index, self.patient_id, target_evaluate_date,site1_0,site1_1,site1_2,site1_3,site1_4,method1_0,method1_1,method1_2,method1_3,method1_4,long_dist_0,long_dist_1,long_dist_2,long_dist_3,long_dist_4,non_target_evaluate_date,site2_0,site2_1,site2_2,site2_3,site2_4,site2_5,method2_0,method2_1,method2_2,method2_3,method2_4,method2_5,status_0,status_1,status_2,status_3,status_4,status_5,is_evaluable_0,is_evaluable_1,is_evaluable_2,is_evaluable_3,is_evaluable_4,is_evaluable_5)
        self.cur.execute(sql)

        sql = "SELECT before_evaluate FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sql)
        page_status = "0"
        for row in self.cur:
            page_status = row[0]

        page_status_new = page_status[0:page_index] + "1" + page_status[(page_index+1):len(page_status)]
        sql = "UPDATE data_status SET before_evaluate=" + page_status_new + " WHERE patient_id='" + self.patient_id + "'"

        self.cur.execute(sql)

        
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
                <a class="active" href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>治疗前评估</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(before_evaluate_page_status)):
            if i==page_index:
                active = ' class="active"'
            else:
                active = "" 
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
        

        self.write("finished")
