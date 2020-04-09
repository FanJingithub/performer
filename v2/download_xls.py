
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
                            db     = 'Test',
                            charset= 'utf8')
    conn.autocommit(1)
    cur = conn.cursor()

    base_col_names = ["name","sex","age","marriage","site","stage","surgery","radiotherapy","chemotherapy"]
    lab_col_names = ["CEA","CA199"]
    pathology_col_names = ["patho_diagnosis","lym_vas_invasion","tot_lymph_node","deep","pni","pos_lymph_node"]
    surgery_col_names = ["resection_way"]
    chemotherapy_col_names = ["chemo_way","chemo_way_other","last_chemo","chemo_time_0","chemo_time_1","chemo_time_2","chemo_way_0","chemo_way_1","chemo_way_2","desc_0","desc_1","desc_2"]
    radiotherapy_col_names = ["radio_count","radio_start","radio_end"]
    follow_up_col_names = ["recurrance"]
    
    base_col_labels = ["姓名","性别","年龄","婚姻情况","肿瘤部位","分期","是否手术","是否放疗","是否化疗"]
    lab_col_labels = ["CEA","CA199"]
    pathology_col_labels = ["病理诊断","脉管癌栓","淋巴结数","浸润深度","神经侵犯","淋巴阳性"]
    surgery_col_labels = ["手术方式"]
    chemotherapy_col_labels = ["化疗方案","化疗方案_other","上次化疗时间","化疗时间_0","化疗时间_1","化疗时间_2","化疗方案_0","化疗方案_1","化疗方案_2","描述_0","描述_1","描述_2"]
    radiotherapy_col_labels = ["放疗次数","放疗开始","放疗结束"]
    follow_up_col_labels = ["是否复发"]
    
    base_col = len(base_col_names)
    lab_col = len(lab_col_names)
    pathology_col = len(pathology_col_names)
    surgery_col = len(surgery_col_names)
    chemotherapy_col = len(chemotherapy_col_names)
    radiotherapy_col = len(radiotherapy_col_names)
    follow_up_col = len(follow_up_col_names)
    
    sql = "SELECT patient_id,base,lab,pathology,surgery,chemotherapy,radiotherapy,follow_up FROM data_status" 
    cur.execute(sql)
    patient_id = []
    base_page_max = 0
    lab_page_max = 0
    pathology_page_max = 0
    surgery_page_max = 0
    chemotherapy_page_max = 0
    radiotherapy_page_max = 0
    follow_up_page_max = 0
    
    for row in cur:
        patient_id.extend([row[0]])
    
        base_page_status = str(row[1])
        base_page_status = str(int(base_page_status[::-1]))[::-1] # delete 0 in tail
        base_page_max = max(base_page_max,len(base_page_status))
        
        lab_page_status = str(row[2])
        lab_page_status = str(int(lab_page_status[::-1]))[::-1] # delete 0 in tail
        lab_page_max = max(lab_page_max,len(lab_page_status))
        
        pathology_page_status = str(row[3])
        pathology_page_status = str(int(pathology_page_status[::-1]))[::-1] # delete 0 in tail
        pathology_page_max = max(pathology_page_max,len(pathology_page_status))
        
        surgery_page_status = str(row[4])
        surgery_page_status = str(int(surgery_page_status[::-1]))[::-1] # delete 0 in tail
        surgery_page_max = max(surgery_page_max,len(surgery_page_status))
        
        chemotherapy_page_status = str(row[5])
        chemotherapy_page_status = str(int(chemotherapy_page_status[::-1]))[::-1] # delete 0 in tail
        chemotherapy_page_max = max(chemotherapy_page_max,len(chemotherapy_page_status))
        
        radiotherapy_page_status = str(row[6])
        radiotherapy_page_status = str(int(radiotherapy_page_status[::-1]))[::-1] # delete 0 in tail
        radiotherapy_page_max = max(radiotherapy_page_max,len(radiotherapy_page_status))
        
        follow_up_page_status = str(row[7])
        follow_up_page_status = str(int(follow_up_page_status[::-1]))[::-1] # delete 0 in tail
        follow_up_page_max = max(follow_up_page_max,len(follow_up_page_status))
        
    row_max = len(patient_id)
    col_max = base_col*base_page_max + lab_col*lab_page_max + pathology_col*pathology_page_max + surgery_col*surgery_page_max + chemotherapy_col*chemotherapy_page_max + radiotherapy_col*radiotherapy_page_max + follow_up_col*follow_up_page_max + 1
    matrix = [list("" for i in range(col_max)) for i in range(row_max+2)]
    for ii in range(len(patient_id)):
        patient = patient_id[ii]
        kk = 0
        
        for i in range(base_page_max):
            page = "base_" + str(i)
            sql = "SELECT name,sex,age,marriage,site,stage,surgery,radiotherapy,chemotherapy FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(base_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(lab_page_max):
            page = "lab_" + str(i)
            sql = "SELECT CEA,CA199 FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(lab_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(pathology_page_max):
            page = "pathology_" + str(i)
            sql = "SELECT patho_diagnosis,lym_vas_invasion,tot_lymph_node,deep,pni,pos_lymph_node FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(pathology_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(surgery_page_max):
            page = "surgery_" + str(i)
            sql = "SELECT resection_way FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(surgery_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(chemotherapy_page_max):
            page = "chemotherapy_" + str(i)
            sql = "SELECT chemo_way,chemo_way_other,last_chemo,chemo_time_0,chemo_time_1,chemo_time_2,chemo_way_0,chemo_way_1,chemo_way_2,desc_0,desc_1,desc_2 FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(chemotherapy_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(radiotherapy_page_max):
            page = "radiotherapy_" + str(i)
            sql = "SELECT radio_count,radio_start,radio_end FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(radiotherapy_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(follow_up_page_max):
            page = "follow_up_" + str(i)
            sql = "SELECT recurrance FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(follow_up_col)]
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
    
    for i in range(pathology_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(pathology_col_names)):
            col_name = pathology_col_names[j]
            col_label = pathology_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(surgery_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(surgery_col_names)):
            col_name = surgery_col_names[j]
            col_label = surgery_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(chemotherapy_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(chemotherapy_col_names)):
            col_name = chemotherapy_col_names[j]
            col_label = chemotherapy_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(radiotherapy_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(radiotherapy_col_names)):
            col_name = radiotherapy_col_names[j]
            col_label = radiotherapy_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(follow_up_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(follow_up_col_names)):
            col_name = follow_up_col_names[j]
            col_label = follow_up_col_labels[j]
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
