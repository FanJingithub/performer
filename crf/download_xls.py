
#!/usr/bin/python
# -*- coding:utf-8 -*-

# Download data into Excel
# Date for Version 2: 2020.04.08

import MySQLdb
import xlrd,xlwt
import time
from datetime import datetime
import os

def getData():

    file_new = xlwt.Workbook(encoding = 'utf-8')
    sheet_1 = file_new.add_sheet('main')

    # prepare some settings
    dateFormat = xlwt.XFStyle()
    dateFormat.num_format_str = 'yyyy-mm-dd'

    warning_style = xlwt.XFStyle()
    fnt = xlwt.Font()
    fnt.colour_index = 2
    warning_style.font = fnt

    tt = 60*60*24
    s_date = int(datetime(1899, 12, 31).timestamp()/tt)-2

    conn = MySQLdb.connect( host   = 'localhost',
                            user   = 'root',
                            passwd = '1',
                            db     = 'CRF',
                            charset= 'utf8')
    conn.autocommit(1)
    cur = conn.cursor()

    base_col_names = ["name","sex","age","first_consult_date","gender","birth_date","rt_num","patient_num","height","weight","tibiao_area","kps","ECOG"]
    physical_exam_col_names = ["physical_exam_1","physical_exam_1_other","annal_dist","manxing","manxing_other","family_tumor","family_tumor_other","self_immune","self_immune_other"]
    lab_col_names = ["exam_date","name_0","name_1","name_2","name_3","name_4","result2_0","result2_1","result2_2","result2_3","result2_4","unit_0","unit_1","unit_2","unit_3","unit_4","valuable_0","valuable_1","valuable_2","valuable_3","valuable_4"]
    special_exam_col_names = ["x_num","ct_num","mri_num","changjin_num","path_num"]
    before_evaluate_col_names = ["target_evaluate_date","site1_0","site1_1","site1_2","site1_3","site1_4","method1_0","method1_1","method1_2","method1_3","method1_4","long_dist_0","long_dist_1","long_dist_2","long_dist_3","long_dist_4","non_target_evaluate_date","site2_0","site2_1","site2_2","site2_3","site2_4","site2_5","method2_0","method2_1","method2_2","method2_3","method2_4","method2_5","status_0","status_1","status_2","status_3","status_4","status_5","is_evaluable_0","is_evaluable_1","is_evaluable_2","is_evaluable_3","is_evaluable_4","is_evaluable_5"]
    after_evaluate_col_names = ["evaluate_date5","site5_0","site5_1","site5_2","site5_3","site5_4","method5_0","method5_1","method5_2","method5_3","method5_4","long_dist2_0","long_dist2_1","long_dist2_2","long_dist2_3","long_dist2_4","evaluate_date6","site6_0","site6_1","site6_2","site6_3","site6_4","method6_0","method6_1","method6_2","method6_3","method6_4","status6_0","status6_1","status6_2","status6_3","status6_4","is_evaluable2_0","is_evaluable2_1","is_evaluable2_2","is_evaluable2_3","is_evaluable2_4","total_result","evaluate_date4"]
    
    base_col_labels = ["姓名","性别","年龄","初诊日期","性别","出生日期","RT号","住院号","身高","体重","体表面积","KPS评分","ECOG体力状况评分(PS)"]
    physical_exam_col_labels = ["体格检查(肛指检查)","体格检查(肛指检查)_other","距肛距离","慢性疾病史","慢性疾病史_other","肿瘤家族史","肿瘤家族史_other","自身免疫性疾病史","自身免疫性疾病史_other"]
    lab_col_labels = ["采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","单位_0","单位_1","单位_2","单位_3","单位_4","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4"]
    special_exam_col_labels = ["X片号","CT号","MRI号","肠镜号","病理号"]
    before_evaluate_col_labels = ["评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","长径_0","长径_1","长径_2","长径_3","长径_4","评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","部位_5","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","测量方法_5","状态_0","状态_1","状态_2","状态_3","状态_4","状态_5","可评估病灶_0","可评估病灶_1","可评估病灶_2","可评估病灶_3","可评估病灶_4","可评估病灶_5"]
    after_evaluate_col_labels = ["评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","长径_0","长径_1","长径_2","长径_3","长径_4","评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","状态（存在或消失）_0","状态（存在或消失）_1","状态（存在或消失）_2","状态（存在或消失）_3","状态（存在或消失）_4","可评估病灶_0","可评估病灶_1","可评估病灶_2","可评估病灶_3","可评估病灶_4","总疗效","评价日期"]
    
    base_col = len(base_col_names)
    physical_exam_col = len(physical_exam_col_names)
    lab_col = len(lab_col_names)
    special_exam_col = len(special_exam_col_names)
    before_evaluate_col = len(before_evaluate_col_names)
    after_evaluate_col = len(after_evaluate_col_names)
    
    sql = "SELECT patient_id,base,physical_exam,lab,special_exam,before_evaluate,after_evaluate FROM data_status" 
    cur.execute(sql)
    patient_id = []
    base_page_max = 0
    physical_exam_page_max = 0
    lab_page_max = 0
    special_exam_page_max = 0
    before_evaluate_page_max = 0
    after_evaluate_page_max = 0
    
    for row in cur:
        patient_id.extend([row[0]])
    
        base_page_status = str(row[1])
        base_page_status = str(int(base_page_status[::-1]))[::-1] # delete 0 in tail
        base_page_max = max(base_page_max,len(base_page_status))
        
        physical_exam_page_status = str(row[2])
        physical_exam_page_status = str(int(physical_exam_page_status[::-1]))[::-1] # delete 0 in tail
        physical_exam_page_max = max(physical_exam_page_max,len(physical_exam_page_status))
        
        lab_page_status = str(row[3])
        lab_page_status = str(int(lab_page_status[::-1]))[::-1] # delete 0 in tail
        lab_page_max = max(lab_page_max,len(lab_page_status))
        
        special_exam_page_status = str(row[4])
        special_exam_page_status = str(int(special_exam_page_status[::-1]))[::-1] # delete 0 in tail
        special_exam_page_max = max(special_exam_page_max,len(special_exam_page_status))
        
        before_evaluate_page_status = str(row[5])
        before_evaluate_page_status = str(int(before_evaluate_page_status[::-1]))[::-1] # delete 0 in tail
        before_evaluate_page_max = max(before_evaluate_page_max,len(before_evaluate_page_status))
        
        after_evaluate_page_status = str(row[6])
        after_evaluate_page_status = str(int(after_evaluate_page_status[::-1]))[::-1] # delete 0 in tail
        after_evaluate_page_max = max(after_evaluate_page_max,len(after_evaluate_page_status))
        
    row_max = len(patient_id)
    col_max = base_col*base_page_max + physical_exam_col*physical_exam_page_max + lab_col*lab_page_max + special_exam_col*special_exam_page_max + before_evaluate_col*before_evaluate_page_max + after_evaluate_col*after_evaluate_page_max + 1
    matrix = [list("" for i in range(col_max)) for i in range(row_max+2)]
    for ii in range(len(patient_id)):
        patient = patient_id[ii]
        kk = 0
        
        for i in range(base_page_max):
            page = "base_" + str(i)
            sql = "SELECT name,sex,age,first_consult_date,gender,birth_date,rt_num,patient_num,height,weight,tibiao_area,kps,ECOG FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(base_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(physical_exam_page_max):
            page = "physical_exam_" + str(i)
            sql = "SELECT physical_exam_1,physical_exam_1_other,annal_dist,manxing,manxing_other,family_tumor,family_tumor_other,self_immune,self_immune_other FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(physical_exam_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(lab_page_max):
            page = "lab_" + str(i)
            sql = "SELECT exam_date,name_0,name_1,name_2,name_3,name_4,result2_0,result2_1,result2_2,result2_3,result2_4,unit_0,unit_1,unit_2,unit_3,unit_4,valuable_0,valuable_1,valuable_2,valuable_3,valuable_4 FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(lab_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(special_exam_page_max):
            page = "special_exam_" + str(i)
            sql = "SELECT x_num,ct_num,mri_num,changjin_num,path_num FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(special_exam_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(before_evaluate_page_max):
            page = "before_evaluate_" + str(i)
            sql = "SELECT target_evaluate_date,site1_0,site1_1,site1_2,site1_3,site1_4,method1_0,method1_1,method1_2,method1_3,method1_4,long_dist_0,long_dist_1,long_dist_2,long_dist_3,long_dist_4,non_target_evaluate_date,site2_0,site2_1,site2_2,site2_3,site2_4,site2_5,method2_0,method2_1,method2_2,method2_3,method2_4,method2_5,status_0,status_1,status_2,status_3,status_4,status_5,is_evaluable_0,is_evaluable_1,is_evaluable_2,is_evaluable_3,is_evaluable_4,is_evaluable_5 FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(before_evaluate_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(after_evaluate_page_max):
            page = "after_evaluate_" + str(i)
            sql = "SELECT evaluate_date5,site5_0,site5_1,site5_2,site5_3,site5_4,method5_0,method5_1,method5_2,method5_3,method5_4,long_dist2_0,long_dist2_1,long_dist2_2,long_dist2_3,long_dist2_4,evaluate_date6,site6_0,site6_1,site6_2,site6_3,site6_4,method6_0,method6_1,method6_2,method6_3,method6_4,status6_0,status6_1,status6_2,status6_3,status6_4,is_evaluable2_0,is_evaluable2_1,is_evaluable2_2,is_evaluable2_3,is_evaluable2_4,total_result,evaluate_date4 FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(after_evaluate_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
    col_names_all = ["patient_id"]
    col_labels_all = ["病例号"]
    for i in range(base_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(base_col_names)):
            col_name = base_col_names[j]
            col_label = base_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(physical_exam_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(physical_exam_col_names)):
            col_name = physical_exam_col_names[j]
            col_label = physical_exam_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(lab_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(lab_col_names)):
            col_name = lab_col_names[j]
            col_label = lab_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(special_exam_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(special_exam_col_names)):
            col_name = special_exam_col_names[j]
            col_label = special_exam_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(before_evaluate_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(before_evaluate_col_names)):
            col_name = before_evaluate_col_names[j]
            col_label = before_evaluate_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(after_evaluate_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(after_evaluate_col_names)):
            col_name = after_evaluate_col_names[j]
            col_label = after_evaluate_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for j in range(col_max):
        matrix[0][j] = col_labels_all[j]
        matrix[1][j] = col_names_all[j]
    for i in range(row_max):
        matrix[i+2][0] = patient_id[i]
    for i in range(row_max+2):
        for j in range(col_max):
            sheet_1.write(i, j, label=matrix[i][j])
            
    # save the file
    new_file = 'download/data.xls'
    if os.path.exists(new_file):
        os.remove(new_file)
    file_new.save(new_file)

getData()
