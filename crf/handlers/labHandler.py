# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class labHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get lab--------------------------')

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
        self.cur.execute('''SELECT lab FROM data_status WHERE patient_id='{0}' '''.format(self.patient_id))
        for row in self.cur:
            page_status = row[0]

        if len(page_status)>page_index:
            exist = 1
            submitted = page_status[page_index]

        res = [self.patient_id, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

        if (submitted=="1"):
            # Get the data from the database
            self.cur.execute('''SELECT patient_id,exam_date0,name0_0,name0_1,name0_2,name0_3,name0_4,name0_5,name0_6,name0_7,result0_0,result0_1,result0_2,result0_3,result0_4,result0_5,result0_6,result0_7,unit0_0,unit0_1,unit0_2,unit0_3,unit0_4,unit0_5,unit0_6,unit0_7,valuable0_0,valuable0_1,valuable0_2,valuable0_3,valuable0_4,valuable0_5,valuable0_6,valuable0_7,exam_date1,name1_0,name1_1,name1_2,name1_3,name1_4,name1_5,name1_6,name1_7,name1_8,name1_9,name1_10,name1_11,name1_12,name1_13,name1_14,name1_15,result1_0,result1_1,result1_2,result1_3,result1_4,result1_5,result1_6,result1_7,result1_8,result1_9,result1_10,result1_11,result1_12,result1_13,result1_14,result1_15,unit1_0,unit1_1,unit1_2,unit1_3,unit1_4,unit1_5,unit1_6,unit1_7,unit1_8,unit1_9,unit1_10,unit1_11,unit1_12,unit1_13,unit1_14,unit1_15,valuable1_0,valuable1_1,valuable1_2,valuable1_3,valuable1_4,valuable1_5,valuable1_6,valuable1_7,valuable1_8,valuable1_9,valuable1_10,valuable1_11,valuable1_12,valuable1_13,valuable1_14,valuable1_15,exam_date2,name2_0,name2_1,name2_2,name2_3,name2_4,name2_5,name2_6,name2_7,result2_0,result2_1,result2_2,result2_3,result2_4,result2_5,result2_6,result2_7,unit2_0,unit2_1,unit2_2,unit2_3,unit2_4,unit2_5,unit2_6,unit2_7,valuable2_0,valuable2_1,valuable2_2,valuable2_3,valuable2_4,valuable2_5,valuable2_6,valuable2_7,exam_date3,name3_0,name3_1,name3_2,name3_3,name3_4,name3_5,name3_6,name3_7,result3_0,result3_1,result3_2,result3_3,result3_4,result3_5,result3_6,result3_7,unit3_0,unit3_1,unit3_2,unit3_3,unit3_4,unit3_5,unit3_6,unit3_7,valuable3_0,valuable3_1,valuable3_2,valuable3_3,valuable3_4,valuable3_5,valuable3_6,valuable3_7,exam_date4,name4_0,name4_1,name4_2,name4_3,name4_4,name4_5,name4_6,name4_7,name4_8,name4_9,result4_0,result4_1,result4_2,result4_3,result4_4,result4_5,result4_6,result4_7,result4_8,result4_9,unit4_0,unit4_1,unit4_2,unit4_3,unit4_4,unit4_5,unit4_6,unit4_7,unit4_8,unit4_9,valuable4_0,valuable4_1,valuable4_2,valuable4_3,valuable4_4,valuable4_5,valuable4_6,valuable4_7,valuable4_8,valuable4_9,exam_date5,name5_0,name5_1,name5_2,name5_3,name5_4,name5_5,name5_6,name5_7,name5_8,name5_9,result5_0,result5_1,result5_2,result5_3,result5_4,result5_5,result5_6,result5_7,result5_8,result5_9,unit5_0,unit5_1,unit5_2,unit5_3,unit5_4,unit5_5,unit5_6,unit5_7,unit5_8,unit5_9,valuable5_0,valuable5_1,valuable5_2,valuable5_3,valuable5_4,valuable5_5,valuable5_6,valuable5_7,valuable5_8,valuable5_9,exam_date6,name6_0,name6_1,name6_2,name6_3,name6_4,name6_5,result6_0,result6_1,result6_2,result6_3,result6_4,result6_5,unit6_0,unit6_1,unit6_2,unit6_3,unit6_4,unit6_5,valuable6_0,valuable6_1,valuable6_2,valuable6_3,valuable6_4,valuable6_5 FROM lab_{0} WHERE patient_id='{1}' '''.format(page_index,self.patient_id))
            for row in self.cur:
                res = row

        if (exist==0):
            page_status = page_status + "0"
            sql = "UPDATE data_status SET lab='" + page_status + "' WHERE patient_id='" + self.patient_id + "'"
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
                <a class="active" href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>检验报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(lab_page_status)):
            if i==page_index:
                active = ' class="active"'
            else:
                active = "" 
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
        

        if page_index>0:
            page_previous = "/lab?patient_id="+self.patient_id+"&page_index="+str(page_index-1)
        else:
            page_previous = "/base?patient_id="+self.patient_id
        if (submitted=="1" and edit=="0"):
            self.render("../html/read_lab_page.html", side_menu=side_menu, page_index=page_index, page_previous=page_previous, patient_id=self.patient_id,  exam_date0=res[1], name0_0=res[2], name0_1=res[3], name0_2=res[4], name0_3=res[5], name0_4=res[6], name0_5=res[7], name0_6=res[8], name0_7=res[9], result0_0=res[10], result0_1=res[11], result0_2=res[12], result0_3=res[13], result0_4=res[14], result0_5=res[15], result0_6=res[16], result0_7=res[17], unit0_0=res[18], unit0_1=res[19], unit0_2=res[20], unit0_3=res[21], unit0_4=res[22], unit0_5=res[23], unit0_6=res[24], unit0_7=res[25], valuable0_0=res[26], valuable0_1=res[27], valuable0_2=res[28], valuable0_3=res[29], valuable0_4=res[30], valuable0_5=res[31], valuable0_6=res[32], valuable0_7=res[33], exam_date1=res[34], name1_0=res[35], name1_1=res[36], name1_2=res[37], name1_3=res[38], name1_4=res[39], name1_5=res[40], name1_6=res[41], name1_7=res[42], name1_8=res[43], name1_9=res[44], name1_10=res[45], name1_11=res[46], name1_12=res[47], name1_13=res[48], name1_14=res[49], name1_15=res[50], result1_0=res[51], result1_1=res[52], result1_2=res[53], result1_3=res[54], result1_4=res[55], result1_5=res[56], result1_6=res[57], result1_7=res[58], result1_8=res[59], result1_9=res[60], result1_10=res[61], result1_11=res[62], result1_12=res[63], result1_13=res[64], result1_14=res[65], result1_15=res[66], unit1_0=res[67], unit1_1=res[68], unit1_2=res[69], unit1_3=res[70], unit1_4=res[71], unit1_5=res[72], unit1_6=res[73], unit1_7=res[74], unit1_8=res[75], unit1_9=res[76], unit1_10=res[77], unit1_11=res[78], unit1_12=res[79], unit1_13=res[80], unit1_14=res[81], unit1_15=res[82], valuable1_0=res[83], valuable1_1=res[84], valuable1_2=res[85], valuable1_3=res[86], valuable1_4=res[87], valuable1_5=res[88], valuable1_6=res[89], valuable1_7=res[90], valuable1_8=res[91], valuable1_9=res[92], valuable1_10=res[93], valuable1_11=res[94], valuable1_12=res[95], valuable1_13=res[96], valuable1_14=res[97], valuable1_15=res[98], exam_date2=res[99], name2_0=res[100], name2_1=res[101], name2_2=res[102], name2_3=res[103], name2_4=res[104], name2_5=res[105], name2_6=res[106], name2_7=res[107], result2_0=res[108], result2_1=res[109], result2_2=res[110], result2_3=res[111], result2_4=res[112], result2_5=res[113], result2_6=res[114], result2_7=res[115], unit2_0=res[116], unit2_1=res[117], unit2_2=res[118], unit2_3=res[119], unit2_4=res[120], unit2_5=res[121], unit2_6=res[122], unit2_7=res[123], valuable2_0=res[124], valuable2_1=res[125], valuable2_2=res[126], valuable2_3=res[127], valuable2_4=res[128], valuable2_5=res[129], valuable2_6=res[130], valuable2_7=res[131], exam_date3=res[132], name3_0=res[133], name3_1=res[134], name3_2=res[135], name3_3=res[136], name3_4=res[137], name3_5=res[138], name3_6=res[139], name3_7=res[140], result3_0=res[141], result3_1=res[142], result3_2=res[143], result3_3=res[144], result3_4=res[145], result3_5=res[146], result3_6=res[147], result3_7=res[148], unit3_0=res[149], unit3_1=res[150], unit3_2=res[151], unit3_3=res[152], unit3_4=res[153], unit3_5=res[154], unit3_6=res[155], unit3_7=res[156], valuable3_0=res[157], valuable3_1=res[158], valuable3_2=res[159], valuable3_3=res[160], valuable3_4=res[161], valuable3_5=res[162], valuable3_6=res[163], valuable3_7=res[164], exam_date4=res[165], name4_0=res[166], name4_1=res[167], name4_2=res[168], name4_3=res[169], name4_4=res[170], name4_5=res[171], name4_6=res[172], name4_7=res[173], name4_8=res[174], name4_9=res[175], result4_0=res[176], result4_1=res[177], result4_2=res[178], result4_3=res[179], result4_4=res[180], result4_5=res[181], result4_6=res[182], result4_7=res[183], result4_8=res[184], result4_9=res[185], unit4_0=res[186], unit4_1=res[187], unit4_2=res[188], unit4_3=res[189], unit4_4=res[190], unit4_5=res[191], unit4_6=res[192], unit4_7=res[193], unit4_8=res[194], unit4_9=res[195], valuable4_0=res[196], valuable4_1=res[197], valuable4_2=res[198], valuable4_3=res[199], valuable4_4=res[200], valuable4_5=res[201], valuable4_6=res[202], valuable4_7=res[203], valuable4_8=res[204], valuable4_9=res[205], exam_date5=res[206], name5_0=res[207], name5_1=res[208], name5_2=res[209], name5_3=res[210], name5_4=res[211], name5_5=res[212], name5_6=res[213], name5_7=res[214], name5_8=res[215], name5_9=res[216], result5_0=res[217], result5_1=res[218], result5_2=res[219], result5_3=res[220], result5_4=res[221], result5_5=res[222], result5_6=res[223], result5_7=res[224], result5_8=res[225], result5_9=res[226], unit5_0=res[227], unit5_1=res[228], unit5_2=res[229], unit5_3=res[230], unit5_4=res[231], unit5_5=res[232], unit5_6=res[233], unit5_7=res[234], unit5_8=res[235], unit5_9=res[236], valuable5_0=res[237], valuable5_1=res[238], valuable5_2=res[239], valuable5_3=res[240], valuable5_4=res[241], valuable5_5=res[242], valuable5_6=res[243], valuable5_7=res[244], valuable5_8=res[245], valuable5_9=res[246], exam_date6=res[247], name6_0=res[248], name6_1=res[249], name6_2=res[250], name6_3=res[251], name6_4=res[252], name6_5=res[253], result6_0=res[254], result6_1=res[255], result6_2=res[256], result6_3=res[257], result6_4=res[258], result6_5=res[259], unit6_0=res[260], unit6_1=res[261], unit6_2=res[262], unit6_3=res[263], unit6_4=res[264], unit6_5=res[265], valuable6_0=res[266], valuable6_1=res[267], valuable6_2=res[268], valuable6_3=res[269], valuable6_4=res[270], valuable6_5=res[271])
        else:
            self.render("../html/edit_lab_page.html", side_menu=side_menu, page_index=page_index, page_previous=page_previous, patient_id=self.patient_id,  exam_date0=res[1], name0_0=res[2], name0_1=res[3], name0_2=res[4], name0_3=res[5], name0_4=res[6], name0_5=res[7], name0_6=res[8], name0_7=res[9], result0_0=res[10], result0_1=res[11], result0_2=res[12], result0_3=res[13], result0_4=res[14], result0_5=res[15], result0_6=res[16], result0_7=res[17], unit0_0=res[18], unit0_1=res[19], unit0_2=res[20], unit0_3=res[21], unit0_4=res[22], unit0_5=res[23], unit0_6=res[24], unit0_7=res[25], valuable0_0=res[26], valuable0_1=res[27], valuable0_2=res[28], valuable0_3=res[29], valuable0_4=res[30], valuable0_5=res[31], valuable0_6=res[32], valuable0_7=res[33], exam_date1=res[34], name1_0=res[35], name1_1=res[36], name1_2=res[37], name1_3=res[38], name1_4=res[39], name1_5=res[40], name1_6=res[41], name1_7=res[42], name1_8=res[43], name1_9=res[44], name1_10=res[45], name1_11=res[46], name1_12=res[47], name1_13=res[48], name1_14=res[49], name1_15=res[50], result1_0=res[51], result1_1=res[52], result1_2=res[53], result1_3=res[54], result1_4=res[55], result1_5=res[56], result1_6=res[57], result1_7=res[58], result1_8=res[59], result1_9=res[60], result1_10=res[61], result1_11=res[62], result1_12=res[63], result1_13=res[64], result1_14=res[65], result1_15=res[66], unit1_0=res[67], unit1_1=res[68], unit1_2=res[69], unit1_3=res[70], unit1_4=res[71], unit1_5=res[72], unit1_6=res[73], unit1_7=res[74], unit1_8=res[75], unit1_9=res[76], unit1_10=res[77], unit1_11=res[78], unit1_12=res[79], unit1_13=res[80], unit1_14=res[81], unit1_15=res[82], valuable1_0=res[83], valuable1_1=res[84], valuable1_2=res[85], valuable1_3=res[86], valuable1_4=res[87], valuable1_5=res[88], valuable1_6=res[89], valuable1_7=res[90], valuable1_8=res[91], valuable1_9=res[92], valuable1_10=res[93], valuable1_11=res[94], valuable1_12=res[95], valuable1_13=res[96], valuable1_14=res[97], valuable1_15=res[98], exam_date2=res[99], name2_0=res[100], name2_1=res[101], name2_2=res[102], name2_3=res[103], name2_4=res[104], name2_5=res[105], name2_6=res[106], name2_7=res[107], result2_0=res[108], result2_1=res[109], result2_2=res[110], result2_3=res[111], result2_4=res[112], result2_5=res[113], result2_6=res[114], result2_7=res[115], unit2_0=res[116], unit2_1=res[117], unit2_2=res[118], unit2_3=res[119], unit2_4=res[120], unit2_5=res[121], unit2_6=res[122], unit2_7=res[123], valuable2_0=res[124], valuable2_1=res[125], valuable2_2=res[126], valuable2_3=res[127], valuable2_4=res[128], valuable2_5=res[129], valuable2_6=res[130], valuable2_7=res[131], exam_date3=res[132], name3_0=res[133], name3_1=res[134], name3_2=res[135], name3_3=res[136], name3_4=res[137], name3_5=res[138], name3_6=res[139], name3_7=res[140], result3_0=res[141], result3_1=res[142], result3_2=res[143], result3_3=res[144], result3_4=res[145], result3_5=res[146], result3_6=res[147], result3_7=res[148], unit3_0=res[149], unit3_1=res[150], unit3_2=res[151], unit3_3=res[152], unit3_4=res[153], unit3_5=res[154], unit3_6=res[155], unit3_7=res[156], valuable3_0=res[157], valuable3_1=res[158], valuable3_2=res[159], valuable3_3=res[160], valuable3_4=res[161], valuable3_5=res[162], valuable3_6=res[163], valuable3_7=res[164], exam_date4=res[165], name4_0=res[166], name4_1=res[167], name4_2=res[168], name4_3=res[169], name4_4=res[170], name4_5=res[171], name4_6=res[172], name4_7=res[173], name4_8=res[174], name4_9=res[175], result4_0=res[176], result4_1=res[177], result4_2=res[178], result4_3=res[179], result4_4=res[180], result4_5=res[181], result4_6=res[182], result4_7=res[183], result4_8=res[184], result4_9=res[185], unit4_0=res[186], unit4_1=res[187], unit4_2=res[188], unit4_3=res[189], unit4_4=res[190], unit4_5=res[191], unit4_6=res[192], unit4_7=res[193], unit4_8=res[194], unit4_9=res[195], valuable4_0=res[196], valuable4_1=res[197], valuable4_2=res[198], valuable4_3=res[199], valuable4_4=res[200], valuable4_5=res[201], valuable4_6=res[202], valuable4_7=res[203], valuable4_8=res[204], valuable4_9=res[205], exam_date5=res[206], name5_0=res[207], name5_1=res[208], name5_2=res[209], name5_3=res[210], name5_4=res[211], name5_5=res[212], name5_6=res[213], name5_7=res[214], name5_8=res[215], name5_9=res[216], result5_0=res[217], result5_1=res[218], result5_2=res[219], result5_3=res[220], result5_4=res[221], result5_5=res[222], result5_6=res[223], result5_7=res[224], result5_8=res[225], result5_9=res[226], unit5_0=res[227], unit5_1=res[228], unit5_2=res[229], unit5_3=res[230], unit5_4=res[231], unit5_5=res[232], unit5_6=res[233], unit5_7=res[234], unit5_8=res[235], unit5_9=res[236], valuable5_0=res[237], valuable5_1=res[238], valuable5_2=res[239], valuable5_3=res[240], valuable5_4=res[241], valuable5_5=res[242], valuable5_6=res[243], valuable5_7=res[244], valuable5_8=res[245], valuable5_9=res[246], exam_date6=res[247], name6_0=res[248], name6_1=res[249], name6_2=res[250], name6_3=res[251], name6_4=res[252], name6_5=res[253], result6_0=res[254], result6_1=res[255], result6_2=res[256], result6_3=res[257], result6_4=res[258], result6_5=res[259], unit6_0=res[260], unit6_1=res[261], unit6_2=res[262], unit6_3=res[263], unit6_4=res[264], unit6_5=res[265], valuable6_0=res[266], valuable6_1=res[267], valuable6_2=res[268], valuable6_3=res[269], valuable6_4=res[270], valuable6_5=res[271])

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        try:
            page_index = self.get_argument("page_index", "0")
        except:
            page_index = "0"
        page_index = int(page_index)
        exam_date0 = self.get_body_argument("exam_date0") 
        name0_0 = self.get_body_argument("name0_0") 
        name0_1 = self.get_body_argument("name0_1") 
        name0_2 = self.get_body_argument("name0_2") 
        name0_3 = self.get_body_argument("name0_3") 
        name0_4 = self.get_body_argument("name0_4") 
        name0_5 = self.get_body_argument("name0_5") 
        name0_6 = self.get_body_argument("name0_6") 
        name0_7 = self.get_body_argument("name0_7") 
        result0_0 = self.get_body_argument("result0_0") 
        result0_1 = self.get_body_argument("result0_1") 
        result0_2 = self.get_body_argument("result0_2") 
        result0_3 = self.get_body_argument("result0_3") 
        result0_4 = self.get_body_argument("result0_4") 
        result0_5 = self.get_body_argument("result0_5") 
        result0_6 = self.get_body_argument("result0_6") 
        result0_7 = self.get_body_argument("result0_7") 
        unit0_0 = self.get_body_argument("unit0_0") 
        unit0_1 = self.get_body_argument("unit0_1") 
        unit0_2 = self.get_body_argument("unit0_2") 
        unit0_3 = self.get_body_argument("unit0_3") 
        unit0_4 = self.get_body_argument("unit0_4") 
        unit0_5 = self.get_body_argument("unit0_5") 
        unit0_6 = self.get_body_argument("unit0_6") 
        unit0_7 = self.get_body_argument("unit0_7") 
        valuable0_0 = self.get_body_argument("valuable0_0") 
        valuable0_1 = self.get_body_argument("valuable0_1") 
        valuable0_2 = self.get_body_argument("valuable0_2") 
        valuable0_3 = self.get_body_argument("valuable0_3") 
        valuable0_4 = self.get_body_argument("valuable0_4") 
        valuable0_5 = self.get_body_argument("valuable0_5") 
        valuable0_6 = self.get_body_argument("valuable0_6") 
        valuable0_7 = self.get_body_argument("valuable0_7") 
        exam_date1 = self.get_body_argument("exam_date1") 
        name1_0 = self.get_body_argument("name1_0") 
        name1_1 = self.get_body_argument("name1_1") 
        name1_2 = self.get_body_argument("name1_2") 
        name1_3 = self.get_body_argument("name1_3") 
        name1_4 = self.get_body_argument("name1_4") 
        name1_5 = self.get_body_argument("name1_5") 
        name1_6 = self.get_body_argument("name1_6") 
        name1_7 = self.get_body_argument("name1_7") 
        name1_8 = self.get_body_argument("name1_8") 
        name1_9 = self.get_body_argument("name1_9") 
        name1_10 = self.get_body_argument("name1_10") 
        name1_11 = self.get_body_argument("name1_11") 
        name1_12 = self.get_body_argument("name1_12") 
        name1_13 = self.get_body_argument("name1_13") 
        name1_14 = self.get_body_argument("name1_14") 
        name1_15 = self.get_body_argument("name1_15") 
        result1_0 = self.get_body_argument("result1_0") 
        result1_1 = self.get_body_argument("result1_1") 
        result1_2 = self.get_body_argument("result1_2") 
        result1_3 = self.get_body_argument("result1_3") 
        result1_4 = self.get_body_argument("result1_4") 
        result1_5 = self.get_body_argument("result1_5") 
        result1_6 = self.get_body_argument("result1_6") 
        result1_7 = self.get_body_argument("result1_7") 
        result1_8 = self.get_body_argument("result1_8") 
        result1_9 = self.get_body_argument("result1_9") 
        result1_10 = self.get_body_argument("result1_10") 
        result1_11 = self.get_body_argument("result1_11") 
        result1_12 = self.get_body_argument("result1_12") 
        result1_13 = self.get_body_argument("result1_13") 
        result1_14 = self.get_body_argument("result1_14") 
        result1_15 = self.get_body_argument("result1_15") 
        unit1_0 = self.get_body_argument("unit1_0") 
        unit1_1 = self.get_body_argument("unit1_1") 
        unit1_2 = self.get_body_argument("unit1_2") 
        unit1_3 = self.get_body_argument("unit1_3") 
        unit1_4 = self.get_body_argument("unit1_4") 
        unit1_5 = self.get_body_argument("unit1_5") 
        unit1_6 = self.get_body_argument("unit1_6") 
        unit1_7 = self.get_body_argument("unit1_7") 
        unit1_8 = self.get_body_argument("unit1_8") 
        unit1_9 = self.get_body_argument("unit1_9") 
        unit1_10 = self.get_body_argument("unit1_10") 
        unit1_11 = self.get_body_argument("unit1_11") 
        unit1_12 = self.get_body_argument("unit1_12") 
        unit1_13 = self.get_body_argument("unit1_13") 
        unit1_14 = self.get_body_argument("unit1_14") 
        unit1_15 = self.get_body_argument("unit1_15") 
        valuable1_0 = self.get_body_argument("valuable1_0") 
        valuable1_1 = self.get_body_argument("valuable1_1") 
        valuable1_2 = self.get_body_argument("valuable1_2") 
        valuable1_3 = self.get_body_argument("valuable1_3") 
        valuable1_4 = self.get_body_argument("valuable1_4") 
        valuable1_5 = self.get_body_argument("valuable1_5") 
        valuable1_6 = self.get_body_argument("valuable1_6") 
        valuable1_7 = self.get_body_argument("valuable1_7") 
        valuable1_8 = self.get_body_argument("valuable1_8") 
        valuable1_9 = self.get_body_argument("valuable1_9") 
        valuable1_10 = self.get_body_argument("valuable1_10") 
        valuable1_11 = self.get_body_argument("valuable1_11") 
        valuable1_12 = self.get_body_argument("valuable1_12") 
        valuable1_13 = self.get_body_argument("valuable1_13") 
        valuable1_14 = self.get_body_argument("valuable1_14") 
        valuable1_15 = self.get_body_argument("valuable1_15") 
        exam_date2 = self.get_body_argument("exam_date2") 
        name2_0 = self.get_body_argument("name2_0") 
        name2_1 = self.get_body_argument("name2_1") 
        name2_2 = self.get_body_argument("name2_2") 
        name2_3 = self.get_body_argument("name2_3") 
        name2_4 = self.get_body_argument("name2_4") 
        name2_5 = self.get_body_argument("name2_5") 
        name2_6 = self.get_body_argument("name2_6") 
        name2_7 = self.get_body_argument("name2_7") 
        result2_0 = self.get_body_argument("result2_0") 
        result2_1 = self.get_body_argument("result2_1") 
        result2_2 = self.get_body_argument("result2_2") 
        result2_3 = self.get_body_argument("result2_3") 
        result2_4 = self.get_body_argument("result2_4") 
        result2_5 = self.get_body_argument("result2_5") 
        result2_6 = self.get_body_argument("result2_6") 
        result2_7 = self.get_body_argument("result2_7") 
        unit2_0 = self.get_body_argument("unit2_0") 
        unit2_1 = self.get_body_argument("unit2_1") 
        unit2_2 = self.get_body_argument("unit2_2") 
        unit2_3 = self.get_body_argument("unit2_3") 
        unit2_4 = self.get_body_argument("unit2_4") 
        unit2_5 = self.get_body_argument("unit2_5") 
        unit2_6 = self.get_body_argument("unit2_6") 
        unit2_7 = self.get_body_argument("unit2_7") 
        valuable2_0 = self.get_body_argument("valuable2_0") 
        valuable2_1 = self.get_body_argument("valuable2_1") 
        valuable2_2 = self.get_body_argument("valuable2_2") 
        valuable2_3 = self.get_body_argument("valuable2_3") 
        valuable2_4 = self.get_body_argument("valuable2_4") 
        valuable2_5 = self.get_body_argument("valuable2_5") 
        valuable2_6 = self.get_body_argument("valuable2_6") 
        valuable2_7 = self.get_body_argument("valuable2_7") 
        exam_date3 = self.get_body_argument("exam_date3") 
        name3_0 = self.get_body_argument("name3_0") 
        name3_1 = self.get_body_argument("name3_1") 
        name3_2 = self.get_body_argument("name3_2") 
        name3_3 = self.get_body_argument("name3_3") 
        name3_4 = self.get_body_argument("name3_4") 
        name3_5 = self.get_body_argument("name3_5") 
        name3_6 = self.get_body_argument("name3_6") 
        name3_7 = self.get_body_argument("name3_7") 
        result3_0 = self.get_body_argument("result3_0") 
        result3_1 = self.get_body_argument("result3_1") 
        result3_2 = self.get_body_argument("result3_2") 
        result3_3 = self.get_body_argument("result3_3") 
        result3_4 = self.get_body_argument("result3_4") 
        result3_5 = self.get_body_argument("result3_5") 
        result3_6 = self.get_body_argument("result3_6") 
        result3_7 = self.get_body_argument("result3_7") 
        unit3_0 = self.get_body_argument("unit3_0") 
        unit3_1 = self.get_body_argument("unit3_1") 
        unit3_2 = self.get_body_argument("unit3_2") 
        unit3_3 = self.get_body_argument("unit3_3") 
        unit3_4 = self.get_body_argument("unit3_4") 
        unit3_5 = self.get_body_argument("unit3_5") 
        unit3_6 = self.get_body_argument("unit3_6") 
        unit3_7 = self.get_body_argument("unit3_7") 
        valuable3_0 = self.get_body_argument("valuable3_0") 
        valuable3_1 = self.get_body_argument("valuable3_1") 
        valuable3_2 = self.get_body_argument("valuable3_2") 
        valuable3_3 = self.get_body_argument("valuable3_3") 
        valuable3_4 = self.get_body_argument("valuable3_4") 
        valuable3_5 = self.get_body_argument("valuable3_5") 
        valuable3_6 = self.get_body_argument("valuable3_6") 
        valuable3_7 = self.get_body_argument("valuable3_7") 
        exam_date4 = self.get_body_argument("exam_date4") 
        name4_0 = self.get_body_argument("name4_0") 
        name4_1 = self.get_body_argument("name4_1") 
        name4_2 = self.get_body_argument("name4_2") 
        name4_3 = self.get_body_argument("name4_3") 
        name4_4 = self.get_body_argument("name4_4") 
        name4_5 = self.get_body_argument("name4_5") 
        name4_6 = self.get_body_argument("name4_6") 
        name4_7 = self.get_body_argument("name4_7") 
        name4_8 = self.get_body_argument("name4_8") 
        name4_9 = self.get_body_argument("name4_9") 
        result4_0 = self.get_body_argument("result4_0") 
        result4_1 = self.get_body_argument("result4_1") 
        result4_2 = self.get_body_argument("result4_2") 
        result4_3 = self.get_body_argument("result4_3") 
        result4_4 = self.get_body_argument("result4_4") 
        result4_5 = self.get_body_argument("result4_5") 
        result4_6 = self.get_body_argument("result4_6") 
        result4_7 = self.get_body_argument("result4_7") 
        result4_8 = self.get_body_argument("result4_8") 
        result4_9 = self.get_body_argument("result4_9") 
        unit4_0 = self.get_body_argument("unit4_0") 
        unit4_1 = self.get_body_argument("unit4_1") 
        unit4_2 = self.get_body_argument("unit4_2") 
        unit4_3 = self.get_body_argument("unit4_3") 
        unit4_4 = self.get_body_argument("unit4_4") 
        unit4_5 = self.get_body_argument("unit4_5") 
        unit4_6 = self.get_body_argument("unit4_6") 
        unit4_7 = self.get_body_argument("unit4_7") 
        unit4_8 = self.get_body_argument("unit4_8") 
        unit4_9 = self.get_body_argument("unit4_9") 
        valuable4_0 = self.get_body_argument("valuable4_0") 
        valuable4_1 = self.get_body_argument("valuable4_1") 
        valuable4_2 = self.get_body_argument("valuable4_2") 
        valuable4_3 = self.get_body_argument("valuable4_3") 
        valuable4_4 = self.get_body_argument("valuable4_4") 
        valuable4_5 = self.get_body_argument("valuable4_5") 
        valuable4_6 = self.get_body_argument("valuable4_6") 
        valuable4_7 = self.get_body_argument("valuable4_7") 
        valuable4_8 = self.get_body_argument("valuable4_8") 
        valuable4_9 = self.get_body_argument("valuable4_9") 
        exam_date5 = self.get_body_argument("exam_date5") 
        name5_0 = self.get_body_argument("name5_0") 
        name5_1 = self.get_body_argument("name5_1") 
        name5_2 = self.get_body_argument("name5_2") 
        name5_3 = self.get_body_argument("name5_3") 
        name5_4 = self.get_body_argument("name5_4") 
        name5_5 = self.get_body_argument("name5_5") 
        name5_6 = self.get_body_argument("name5_6") 
        name5_7 = self.get_body_argument("name5_7") 
        name5_8 = self.get_body_argument("name5_8") 
        name5_9 = self.get_body_argument("name5_9") 
        result5_0 = self.get_body_argument("result5_0") 
        result5_1 = self.get_body_argument("result5_1") 
        result5_2 = self.get_body_argument("result5_2") 
        result5_3 = self.get_body_argument("result5_3") 
        result5_4 = self.get_body_argument("result5_4") 
        result5_5 = self.get_body_argument("result5_5") 
        result5_6 = self.get_body_argument("result5_6") 
        result5_7 = self.get_body_argument("result5_7") 
        result5_8 = self.get_body_argument("result5_8") 
        result5_9 = self.get_body_argument("result5_9") 
        unit5_0 = self.get_body_argument("unit5_0") 
        unit5_1 = self.get_body_argument("unit5_1") 
        unit5_2 = self.get_body_argument("unit5_2") 
        unit5_3 = self.get_body_argument("unit5_3") 
        unit5_4 = self.get_body_argument("unit5_4") 
        unit5_5 = self.get_body_argument("unit5_5") 
        unit5_6 = self.get_body_argument("unit5_6") 
        unit5_7 = self.get_body_argument("unit5_7") 
        unit5_8 = self.get_body_argument("unit5_8") 
        unit5_9 = self.get_body_argument("unit5_9") 
        valuable5_0 = self.get_body_argument("valuable5_0") 
        valuable5_1 = self.get_body_argument("valuable5_1") 
        valuable5_2 = self.get_body_argument("valuable5_2") 
        valuable5_3 = self.get_body_argument("valuable5_3") 
        valuable5_4 = self.get_body_argument("valuable5_4") 
        valuable5_5 = self.get_body_argument("valuable5_5") 
        valuable5_6 = self.get_body_argument("valuable5_6") 
        valuable5_7 = self.get_body_argument("valuable5_7") 
        valuable5_8 = self.get_body_argument("valuable5_8") 
        valuable5_9 = self.get_body_argument("valuable5_9") 
        exam_date6 = self.get_body_argument("exam_date6") 
        name6_0 = self.get_body_argument("name6_0") 
        name6_1 = self.get_body_argument("name6_1") 
        name6_2 = self.get_body_argument("name6_2") 
        name6_3 = self.get_body_argument("name6_3") 
        name6_4 = self.get_body_argument("name6_4") 
        name6_5 = self.get_body_argument("name6_5") 
        result6_0 = self.get_body_argument("result6_0") 
        result6_1 = self.get_body_argument("result6_1") 
        result6_2 = self.get_body_argument("result6_2") 
        result6_3 = self.get_body_argument("result6_3") 
        result6_4 = self.get_body_argument("result6_4") 
        result6_5 = self.get_body_argument("result6_5") 
        unit6_0 = self.get_body_argument("unit6_0") 
        unit6_1 = self.get_body_argument("unit6_1") 
        unit6_2 = self.get_body_argument("unit6_2") 
        unit6_3 = self.get_body_argument("unit6_3") 
        unit6_4 = self.get_body_argument("unit6_4") 
        unit6_5 = self.get_body_argument("unit6_5") 
        valuable6_0 = self.get_body_argument("valuable6_0") 
        valuable6_1 = self.get_body_argument("valuable6_1") 
        valuable6_2 = self.get_body_argument("valuable6_2") 
        valuable6_3 = self.get_body_argument("valuable6_3") 
        valuable6_4 = self.get_body_argument("valuable6_4") 
        valuable6_5 = self.get_body_argument("valuable6_5") 
        
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'root',
                                passwd = '1',
                                db     = 'CRF',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        sql = '''REPLACE INTO lab_{0} (patient_id, exam_date0, name0_0, name0_1, name0_2, name0_3, name0_4, name0_5, name0_6, name0_7, result0_0, result0_1, result0_2, result0_3, result0_4, result0_5, result0_6, result0_7, unit0_0, unit0_1, unit0_2, unit0_3, unit0_4, unit0_5, unit0_6, unit0_7, valuable0_0, valuable0_1, valuable0_2, valuable0_3, valuable0_4, valuable0_5, valuable0_6, valuable0_7, exam_date1, name1_0, name1_1, name1_2, name1_3, name1_4, name1_5, name1_6, name1_7, name1_8, name1_9, name1_10, name1_11, name1_12, name1_13, name1_14, name1_15, result1_0, result1_1, result1_2, result1_3, result1_4, result1_5, result1_6, result1_7, result1_8, result1_9, result1_10, result1_11, result1_12, result1_13, result1_14, result1_15, unit1_0, unit1_1, unit1_2, unit1_3, unit1_4, unit1_5, unit1_6, unit1_7, unit1_8, unit1_9, unit1_10, unit1_11, unit1_12, unit1_13, unit1_14, unit1_15, valuable1_0, valuable1_1, valuable1_2, valuable1_3, valuable1_4, valuable1_5, valuable1_6, valuable1_7, valuable1_8, valuable1_9, valuable1_10, valuable1_11, valuable1_12, valuable1_13, valuable1_14, valuable1_15, exam_date2, name2_0, name2_1, name2_2, name2_3, name2_4, name2_5, name2_6, name2_7, result2_0, result2_1, result2_2, result2_3, result2_4, result2_5, result2_6, result2_7, unit2_0, unit2_1, unit2_2, unit2_3, unit2_4, unit2_5, unit2_6, unit2_7, valuable2_0, valuable2_1, valuable2_2, valuable2_3, valuable2_4, valuable2_5, valuable2_6, valuable2_7, exam_date3, name3_0, name3_1, name3_2, name3_3, name3_4, name3_5, name3_6, name3_7, result3_0, result3_1, result3_2, result3_3, result3_4, result3_5, result3_6, result3_7, unit3_0, unit3_1, unit3_2, unit3_3, unit3_4, unit3_5, unit3_6, unit3_7, valuable3_0, valuable3_1, valuable3_2, valuable3_3, valuable3_4, valuable3_5, valuable3_6, valuable3_7, exam_date4, name4_0, name4_1, name4_2, name4_3, name4_4, name4_5, name4_6, name4_7, name4_8, name4_9, result4_0, result4_1, result4_2, result4_3, result4_4, result4_5, result4_6, result4_7, result4_8, result4_9, unit4_0, unit4_1, unit4_2, unit4_3, unit4_4, unit4_5, unit4_6, unit4_7, unit4_8, unit4_9, valuable4_0, valuable4_1, valuable4_2, valuable4_3, valuable4_4, valuable4_5, valuable4_6, valuable4_7, valuable4_8, valuable4_9, exam_date5, name5_0, name5_1, name5_2, name5_3, name5_4, name5_5, name5_6, name5_7, name5_8, name5_9, result5_0, result5_1, result5_2, result5_3, result5_4, result5_5, result5_6, result5_7, result5_8, result5_9, unit5_0, unit5_1, unit5_2, unit5_3, unit5_4, unit5_5, unit5_6, unit5_7, unit5_8, unit5_9, valuable5_0, valuable5_1, valuable5_2, valuable5_3, valuable5_4, valuable5_5, valuable5_6, valuable5_7, valuable5_8, valuable5_9, exam_date6, name6_0, name6_1, name6_2, name6_3, name6_4, name6_5, result6_0, result6_1, result6_2, result6_3, result6_4, result6_5, unit6_0, unit6_1, unit6_2, unit6_3, unit6_4, unit6_5, valuable6_0, valuable6_1, valuable6_2, valuable6_3, valuable6_4, valuable6_5) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}', '{30}', '{31}', '{32}', '{33}', '{34}', '{35}', '{36}', '{37}', '{38}', '{39}', '{40}', '{41}', '{42}', '{43}', '{44}', '{45}', '{46}', '{47}', '{48}', '{49}', '{50}', '{51}', '{52}', '{53}', '{54}', '{55}', '{56}', '{57}', '{58}', '{59}', '{60}', '{61}', '{62}', '{63}', '{64}', '{65}', '{66}', '{67}', '{68}', '{69}', '{70}', '{71}', '{72}', '{73}', '{74}', '{75}', '{76}', '{77}', '{78}', '{79}', '{80}', '{81}', '{82}', '{83}', '{84}', '{85}', '{86}', '{87}', '{88}', '{89}', '{90}', '{91}', '{92}', '{93}', '{94}', '{95}', '{96}', '{97}', '{98}', '{99}', '{100}', '{101}', '{102}', '{103}', '{104}', '{105}', '{106}', '{107}', '{108}', '{109}', '{110}', '{111}', '{112}', '{113}', '{114}', '{115}', '{116}', '{117}', '{118}', '{119}', '{120}', '{121}', '{122}', '{123}', '{124}', '{125}', '{126}', '{127}', '{128}', '{129}', '{130}', '{131}', '{132}', '{133}', '{134}', '{135}', '{136}', '{137}', '{138}', '{139}', '{140}', '{141}', '{142}', '{143}', '{144}', '{145}', '{146}', '{147}', '{148}', '{149}', '{150}', '{151}', '{152}', '{153}', '{154}', '{155}', '{156}', '{157}', '{158}', '{159}', '{160}', '{161}', '{162}', '{163}', '{164}', '{165}', '{166}', '{167}', '{168}', '{169}', '{170}', '{171}', '{172}', '{173}', '{174}', '{175}', '{176}', '{177}', '{178}', '{179}', '{180}', '{181}', '{182}', '{183}', '{184}', '{185}', '{186}', '{187}', '{188}', '{189}', '{190}', '{191}', '{192}', '{193}', '{194}', '{195}', '{196}', '{197}', '{198}', '{199}', '{200}', '{201}', '{202}', '{203}', '{204}', '{205}', '{206}', '{207}', '{208}', '{209}', '{210}', '{211}', '{212}', '{213}', '{214}', '{215}', '{216}', '{217}', '{218}', '{219}', '{220}', '{221}', '{222}', '{223}', '{224}', '{225}', '{226}', '{227}', '{228}', '{229}', '{230}', '{231}', '{232}', '{233}', '{234}', '{235}', '{236}', '{237}', '{238}', '{239}', '{240}', '{241}', '{242}', '{243}', '{244}', '{245}', '{246}', '{247}', '{248}', '{249}', '{250}', '{251}', '{252}', '{253}', '{254}', '{255}', '{256}', '{257}', '{258}', '{259}', '{260}', '{261}', '{262}', '{263}', '{264}', '{265}', '{266}', '{267}', '{268}', '{269}', '{270}', '{271}', '{272}') '''.format(page_index, self.patient_id, exam_date0,name0_0,name0_1,name0_2,name0_3,name0_4,name0_5,name0_6,name0_7,result0_0,result0_1,result0_2,result0_3,result0_4,result0_5,result0_6,result0_7,unit0_0,unit0_1,unit0_2,unit0_3,unit0_4,unit0_5,unit0_6,unit0_7,valuable0_0,valuable0_1,valuable0_2,valuable0_3,valuable0_4,valuable0_5,valuable0_6,valuable0_7,exam_date1,name1_0,name1_1,name1_2,name1_3,name1_4,name1_5,name1_6,name1_7,name1_8,name1_9,name1_10,name1_11,name1_12,name1_13,name1_14,name1_15,result1_0,result1_1,result1_2,result1_3,result1_4,result1_5,result1_6,result1_7,result1_8,result1_9,result1_10,result1_11,result1_12,result1_13,result1_14,result1_15,unit1_0,unit1_1,unit1_2,unit1_3,unit1_4,unit1_5,unit1_6,unit1_7,unit1_8,unit1_9,unit1_10,unit1_11,unit1_12,unit1_13,unit1_14,unit1_15,valuable1_0,valuable1_1,valuable1_2,valuable1_3,valuable1_4,valuable1_5,valuable1_6,valuable1_7,valuable1_8,valuable1_9,valuable1_10,valuable1_11,valuable1_12,valuable1_13,valuable1_14,valuable1_15,exam_date2,name2_0,name2_1,name2_2,name2_3,name2_4,name2_5,name2_6,name2_7,result2_0,result2_1,result2_2,result2_3,result2_4,result2_5,result2_6,result2_7,unit2_0,unit2_1,unit2_2,unit2_3,unit2_4,unit2_5,unit2_6,unit2_7,valuable2_0,valuable2_1,valuable2_2,valuable2_3,valuable2_4,valuable2_5,valuable2_6,valuable2_7,exam_date3,name3_0,name3_1,name3_2,name3_3,name3_4,name3_5,name3_6,name3_7,result3_0,result3_1,result3_2,result3_3,result3_4,result3_5,result3_6,result3_7,unit3_0,unit3_1,unit3_2,unit3_3,unit3_4,unit3_5,unit3_6,unit3_7,valuable3_0,valuable3_1,valuable3_2,valuable3_3,valuable3_4,valuable3_5,valuable3_6,valuable3_7,exam_date4,name4_0,name4_1,name4_2,name4_3,name4_4,name4_5,name4_6,name4_7,name4_8,name4_9,result4_0,result4_1,result4_2,result4_3,result4_4,result4_5,result4_6,result4_7,result4_8,result4_9,unit4_0,unit4_1,unit4_2,unit4_3,unit4_4,unit4_5,unit4_6,unit4_7,unit4_8,unit4_9,valuable4_0,valuable4_1,valuable4_2,valuable4_3,valuable4_4,valuable4_5,valuable4_6,valuable4_7,valuable4_8,valuable4_9,exam_date5,name5_0,name5_1,name5_2,name5_3,name5_4,name5_5,name5_6,name5_7,name5_8,name5_9,result5_0,result5_1,result5_2,result5_3,result5_4,result5_5,result5_6,result5_7,result5_8,result5_9,unit5_0,unit5_1,unit5_2,unit5_3,unit5_4,unit5_5,unit5_6,unit5_7,unit5_8,unit5_9,valuable5_0,valuable5_1,valuable5_2,valuable5_3,valuable5_4,valuable5_5,valuable5_6,valuable5_7,valuable5_8,valuable5_9,exam_date6,name6_0,name6_1,name6_2,name6_3,name6_4,name6_5,result6_0,result6_1,result6_2,result6_3,result6_4,result6_5,unit6_0,unit6_1,unit6_2,unit6_3,unit6_4,unit6_5,valuable6_0,valuable6_1,valuable6_2,valuable6_3,valuable6_4,valuable6_5)
        self.cur.execute(sql)

        sql = "SELECT lab FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sql)
        page_status = "0"
        for row in self.cur:
            page_status = row[0]

        page_status_new = page_status[0:page_index] + "1" + page_status[(page_index+1):len(page_status)]
        sql = "UPDATE data_status SET lab=" + page_status_new + " WHERE patient_id='" + self.patient_id + "'"

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
                <a class="active" href="javascript:;">
                    <i class="fa fa-tasks"></i>
                    <span>检验报告</span>
                </a>
                <ul class="sub">'''
        active = ''
        for i in range(len(lab_page_status)):
            if i==page_index:
                active = ' class="active"'
            else:
                active = "" 
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
        

        self.write("finished")
