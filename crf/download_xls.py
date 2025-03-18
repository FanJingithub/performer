
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

    base_col_names = ["name","sex","age","first_consult_date","birth_date","rt_num","patient_num","height","weight","tibiao_area","kps","ECOG"]
    physical_exam_col_names = ["physical_exam_1","physical_exam_1_other","annal_dist","manxing","manxing_other","family_tumor","family_tumor_other","self_immune","self_immune_other"]
    lab_col_names = ["exam_date0","name0_0","name0_1","name0_2","name0_3","name0_4","name0_5","name0_6","name0_7","result0_0","result0_1","result0_2","result0_3","result0_4","result0_5","result0_6","result0_7","unit0_0","unit0_1","unit0_2","unit0_3","unit0_4","unit0_5","unit0_6","unit0_7","valuable0_0","valuable0_1","valuable0_2","valuable0_3","valuable0_4","valuable0_5","valuable0_6","valuable0_7","exam_date1","name1_0","name1_1","name1_2","name1_3","name1_4","name1_5","name1_6","name1_7","name1_8","name1_9","name1_10","name1_11","name1_12","name1_13","name1_14","name1_15","result1_0","result1_1","result1_2","result1_3","result1_4","result1_5","result1_6","result1_7","result1_8","result1_9","result1_10","result1_11","result1_12","result1_13","result1_14","result1_15","unit1_0","unit1_1","unit1_2","unit1_3","unit1_4","unit1_5","unit1_6","unit1_7","unit1_8","unit1_9","unit1_10","unit1_11","unit1_12","unit1_13","unit1_14","unit1_15","valuable1_0","valuable1_1","valuable1_2","valuable1_3","valuable1_4","valuable1_5","valuable1_6","valuable1_7","valuable1_8","valuable1_9","valuable1_10","valuable1_11","valuable1_12","valuable1_13","valuable1_14","valuable1_15","exam_date2","name2_0","name2_1","name2_2","name2_3","name2_4","name2_5","name2_6","name2_7","result2_0","result2_1","result2_2","result2_3","result2_4","result2_5","result2_6","result2_7","unit2_0","unit2_1","unit2_2","unit2_3","unit2_4","unit2_5","unit2_6","unit2_7","valuable2_0","valuable2_1","valuable2_2","valuable2_3","valuable2_4","valuable2_5","valuable2_6","valuable2_7","exam_date3","name3_0","name3_1","name3_2","name3_3","name3_4","name3_5","name3_6","name3_7","result3_0","result3_1","result3_2","result3_3","result3_4","result3_5","result3_6","result3_7","unit3_0","unit3_1","unit3_2","unit3_3","unit3_4","unit3_5","unit3_6","unit3_7","valuable3_0","valuable3_1","valuable3_2","valuable3_3","valuable3_4","valuable3_5","valuable3_6","valuable3_7","exam_date4","name4_0","name4_1","name4_2","name4_3","name4_4","name4_5","name4_6","name4_7","name4_8","name4_9","result4_0","result4_1","result4_2","result4_3","result4_4","result4_5","result4_6","result4_7","result4_8","result4_9","unit4_0","unit4_1","unit4_2","unit4_3","unit4_4","unit4_5","unit4_6","unit4_7","unit4_8","unit4_9","valuable4_0","valuable4_1","valuable4_2","valuable4_3","valuable4_4","valuable4_5","valuable4_6","valuable4_7","valuable4_8","valuable4_9","exam_date5","name5_0","name5_1","name5_2","name5_3","name5_4","name5_5","name5_6","name5_7","name5_8","name5_9","result5_0","result5_1","result5_2","result5_3","result5_4","result5_5","result5_6","result5_7","result5_8","result5_9","unit5_0","unit5_1","unit5_2","unit5_3","unit5_4","unit5_5","unit5_6","unit5_7","unit5_8","unit5_9","valuable5_0","valuable5_1","valuable5_2","valuable5_3","valuable5_4","valuable5_5","valuable5_6","valuable5_7","valuable5_8","valuable5_9","exam_date6","name6_0","name6_1","name6_2","name6_3","name6_4","name6_5","result6_0","result6_1","result6_2","result6_3","result6_4","result6_5","unit6_0","unit6_1","unit6_2","unit6_3","unit6_4","unit6_5","valuable6_0","valuable6_1","valuable6_2","valuable6_3","valuable6_4","valuable6_5"]
    special_exam_col_names = ["x_num","ct_num","mri_num","changjin_num","path_num"]
    radiology_colonoscopy_col_names = ["chest_CT_result","chest_CT_result_other","abdomen_CT_result","abdomen_CT_result_other","pelvic_MRI_result","tumor_dist_from_anal","tumour_circle","tumor_length","can_pass","t_stage","n_stage"]
    colonoscopy_pathology_col_names = ["first_path_diagnose_date","pathology_type","pathology_type_other","degree_of_differentiation"]
    msi_mmr_col_names = ["msi_result","mmr_result"]
    gene_col_names = ["gene_result"]
    clinical_stage_col_names = ["c_t_stage","c_n_stage","c_m_stage","final_stage"]
    before_evaluate_col_names = ["target_evaluate_date","site1_0","site1_1","site1_2","site1_3","site1_4","method1_0","method1_1","method1_2","method1_3","method1_4","long_dist_0","long_dist_1","long_dist_2","long_dist_3","long_dist_4","non_target_evaluate_date","site2_0","site2_1","site2_2","site2_3","site2_4","site2_5","method2_0","method2_1","method2_2","method2_3","method2_4","method2_5","status_0","status_1","status_2","status_3","status_4","status_5","is_evaluable_0","is_evaluable_1","is_evaluable_2","is_evaluable_3","is_evaluable_4","is_evaluable_5"]
    treatment_col_names = ["group","treat_start_time","treat_end_time","treat_count","stop_reason","progress_time","dead_time"]
    after_evaluate_col_names = ["evaluate_date5","site5_0","site5_1","site5_2","site5_3","site5_4","method5_0","method5_1","method5_2","method5_3","method5_4","long_dist2_0","long_dist2_1","long_dist2_2","long_dist2_3","long_dist2_4","evaluate_date6","site6_0","site6_1","site6_2","site6_3","site6_4","method6_0","method6_1","method6_2","method6_3","method6_4","status6_0","status6_1","status6_2","status6_3","status6_4","is_evaluable2_0","is_evaluable2_1","is_evaluable2_2","is_evaluable2_3","is_evaluable2_4","total_result","evaluate_date4"]
    adverse_event_col_names = ["adverse_type","start_time","end_time","nci_ctc","disposal","disposal_other","outcome","drug_relation"]
    concomitant_medication_col_names = ["drug","start_time","end_time","dose","method","reason"]
    follow_up_col_names = ["follow_up_date","is_liver_metastases_resection","liver_metastases_resection_date","liver_metastases_resection_patho","is_progress","progress_date","live_state","dead_date","last_date_before_missing"]
    
    base_col_labels = ["姓名","性别","年龄","初诊日期","出生日期","RT号","住院号","身高","体重","体表面积","KPS评分","ECOG体力状况评分(PS)"]
    physical_exam_col_labels = ["体格检查(肛指检查)","体格检查(肛指检查)_other","距肛距离","慢性疾病史","慢性疾病史_other","肿瘤家族史","肿瘤家族史_other","自身免疫性疾病史","自身免疫性疾病史_other"]
    lab_col_labels = ["采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查项目_6","检查项目_7","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","检查结果_6","检查结果_7","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","单位_6","单位_7","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5","是否有临床意义_6","是否有临床意义_7","采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查项目_6","检查项目_7","检查项目_8","检查项目_9","检查项目_10","检查项目_11","检查项目_12","检查项目_13","检查项目_14","检查项目_15","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","检查结果_6","检查结果_7","检查结果_8","检查结果_9","检查结果_10","检查结果_11","检查结果_12","检查结果_13","检查结果_14","检查结果_15","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","单位_6","单位_7","单位_8","单位_9","单位_10","单位_11","单位_12","单位_13","单位_14","单位_15","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5","是否有临床意义_6","是否有临床意义_7","是否有临床意义_8","是否有临床意义_9","是否有临床意义_10","是否有临床意义_11","是否有临床意义_12","是否有临床意义_13","是否有临床意义_14","是否有临床意义_15","采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查项目_6","检查项目_7","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","检查结果_6","检查结果_7","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","单位_6","单位_7","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5","是否有临床意义_6","是否有临床意义_7","采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查项目_6","检查项目_7","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","检查结果_6","检查结果_7","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","单位_6","单位_7","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5","是否有临床意义_6","是否有临床意义_7","采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查项目_6","检查项目_7","检查项目_8","检查项目_9","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","检查结果_6","检查结果_7","检查结果_8","检查结果_9","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","单位_6","单位_7","单位_8","单位_9","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5","是否有临床意义_6","是否有临床意义_7","是否有临床意义_8","是否有临床意义_9","采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查项目_6","检查项目_7","检查项目_8","检查项目_9","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","检查结果_6","检查结果_7","检查结果_8","检查结果_9","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","单位_6","单位_7","单位_8","单位_9","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5","是否有临床意义_6","是否有临床意义_7","是否有临床意义_8","是否有临床意义_9","采样日期","检查项目_0","检查项目_1","检查项目_2","检查项目_3","检查项目_4","检查项目_5","检查结果_0","检查结果_1","检查结果_2","检查结果_3","检查结果_4","检查结果_5","单位_0","单位_1","单位_2","单位_3","单位_4","单位_5","是否有临床意义_0","是否有临床意义_1","是否有临床意义_2","是否有临床意义_3","是否有临床意义_4","是否有临床意义_5"]
    special_exam_col_labels = ["X片号","CT号","MRI号","肠镜号","病理号"]
    radiology_colonoscopy_col_labels = ["胸部CT结果","胸部CT结果_other","腹部CT结果","腹部CT结果_other","盆腔MRI结果","肿瘤距肛距离","环周","肿瘤长度","肠镜是否可通过","T分期","N分期"]
    colonoscopy_pathology_col_labels = ["首次病理学确诊日期","病理类型","病理类型_other","分化程度"]
    msi_mmr_col_labels = ["MSI评价","MMR评价"]
    gene_col_labels = ["基因检测结果描述"]
    clinical_stage_col_labels = ["cT","cN","cM","总分期"]
    before_evaluate_col_labels = ["评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","长径_0","长径_1","长径_2","长径_3","长径_4","评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","部位_5","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","测量方法_5","状态_0","状态_1","状态_2","状态_3","状态_4","状态_5","可评估病灶_0","可评估病灶_1","可评估病灶_2","可评估病灶_3","可评估病灶_4","可评估病灶_5"]
    treatment_col_labels = ["分组","首次治疗时间","末次治疗时间","一共完成化疗次数","化疗终止原因","病情进展日期(如果出现进展)","死亡日期(如果死亡)"]
    after_evaluate_col_labels = ["评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","长径_0","长径_1","长径_2","长径_3","长径_4","评价日期","部位_0","部位_1","部位_2","部位_3","部位_4","测量方法_0","测量方法_1","测量方法_2","测量方法_3","测量方法_4","状态（存在或消失）_0","状态（存在或消失）_1","状态（存在或消失）_2","状态（存在或消失）_3","状态（存在或消失）_4","可评估病灶_0","可评估病灶_1","可评估病灶_2","可评估病灶_3","可评估病灶_4","总疗效","评价日期"]
    adverse_event_col_labels = ["不良事件类型","发生日期","结束日期","NCI-CTC分级","采取措施","采取措施_other","转归","与研究药物关系"]
    concomitant_medication_col_labels = ["药名","开始日期","结束日期","剂量","用法","使用原因"]
    follow_up_col_labels = ["随访日期","是否有肝转移手术切除","肝转移切除日期","肝转移切除术后病理","是否进展","进展日期(如果进展)","生存状态","死亡日期(如果死亡)","末次随访联系日期"]
    
    base_col = len(base_col_names)
    physical_exam_col = len(physical_exam_col_names)
    lab_col = len(lab_col_names)
    special_exam_col = len(special_exam_col_names)
    radiology_colonoscopy_col = len(radiology_colonoscopy_col_names)
    colonoscopy_pathology_col = len(colonoscopy_pathology_col_names)
    msi_mmr_col = len(msi_mmr_col_names)
    gene_col = len(gene_col_names)
    clinical_stage_col = len(clinical_stage_col_names)
    before_evaluate_col = len(before_evaluate_col_names)
    treatment_col = len(treatment_col_names)
    after_evaluate_col = len(after_evaluate_col_names)
    adverse_event_col = len(adverse_event_col_names)
    concomitant_medication_col = len(concomitant_medication_col_names)
    follow_up_col = len(follow_up_col_names)
    
    sql = "SELECT patient_id,base,physical_exam,lab,special_exam,radiology_colonoscopy,colonoscopy_pathology,msi_mmr,gene,clinical_stage,before_evaluate,treatment,after_evaluate,adverse_event,concomitant_medication,follow_up FROM data_status" 
    cur.execute(sql)
    patient_id = []
    base_page_max = 0
    physical_exam_page_max = 0
    lab_page_max = 0
    special_exam_page_max = 0
    radiology_colonoscopy_page_max = 0
    colonoscopy_pathology_page_max = 0
    msi_mmr_page_max = 0
    gene_page_max = 0
    clinical_stage_page_max = 0
    before_evaluate_page_max = 0
    treatment_page_max = 0
    after_evaluate_page_max = 0
    adverse_event_page_max = 0
    concomitant_medication_page_max = 0
    follow_up_page_max = 0
    
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
        
        radiology_colonoscopy_page_status = str(row[5])
        radiology_colonoscopy_page_status = str(int(radiology_colonoscopy_page_status[::-1]))[::-1] # delete 0 in tail
        radiology_colonoscopy_page_max = max(radiology_colonoscopy_page_max,len(radiology_colonoscopy_page_status))
        
        colonoscopy_pathology_page_status = str(row[6])
        colonoscopy_pathology_page_status = str(int(colonoscopy_pathology_page_status[::-1]))[::-1] # delete 0 in tail
        colonoscopy_pathology_page_max = max(colonoscopy_pathology_page_max,len(colonoscopy_pathology_page_status))
        
        msi_mmr_page_status = str(row[7])
        msi_mmr_page_status = str(int(msi_mmr_page_status[::-1]))[::-1] # delete 0 in tail
        msi_mmr_page_max = max(msi_mmr_page_max,len(msi_mmr_page_status))
        
        gene_page_status = str(row[8])
        gene_page_status = str(int(gene_page_status[::-1]))[::-1] # delete 0 in tail
        gene_page_max = max(gene_page_max,len(gene_page_status))
        
        clinical_stage_page_status = str(row[9])
        clinical_stage_page_status = str(int(clinical_stage_page_status[::-1]))[::-1] # delete 0 in tail
        clinical_stage_page_max = max(clinical_stage_page_max,len(clinical_stage_page_status))
        
        before_evaluate_page_status = str(row[10])
        before_evaluate_page_status = str(int(before_evaluate_page_status[::-1]))[::-1] # delete 0 in tail
        before_evaluate_page_max = max(before_evaluate_page_max,len(before_evaluate_page_status))
        
        treatment_page_status = str(row[11])
        treatment_page_status = str(int(treatment_page_status[::-1]))[::-1] # delete 0 in tail
        treatment_page_max = max(treatment_page_max,len(treatment_page_status))
        
        after_evaluate_page_status = str(row[12])
        after_evaluate_page_status = str(int(after_evaluate_page_status[::-1]))[::-1] # delete 0 in tail
        after_evaluate_page_max = max(after_evaluate_page_max,len(after_evaluate_page_status))
        
        adverse_event_page_status = str(row[13])
        adverse_event_page_status = str(int(adverse_event_page_status[::-1]))[::-1] # delete 0 in tail
        adverse_event_page_max = max(adverse_event_page_max,len(adverse_event_page_status))
        
        concomitant_medication_page_status = str(row[14])
        concomitant_medication_page_status = str(int(concomitant_medication_page_status[::-1]))[::-1] # delete 0 in tail
        concomitant_medication_page_max = max(concomitant_medication_page_max,len(concomitant_medication_page_status))
        
        follow_up_page_status = str(row[15])
        follow_up_page_status = str(int(follow_up_page_status[::-1]))[::-1] # delete 0 in tail
        follow_up_page_max = max(follow_up_page_max,len(follow_up_page_status))
        
    row_max = len(patient_id)
    col_max = base_col*base_page_max + physical_exam_col*physical_exam_page_max + lab_col*lab_page_max + special_exam_col*special_exam_page_max + radiology_colonoscopy_col*radiology_colonoscopy_page_max + colonoscopy_pathology_col*colonoscopy_pathology_page_max + msi_mmr_col*msi_mmr_page_max + gene_col*gene_page_max + clinical_stage_col*clinical_stage_page_max + before_evaluate_col*before_evaluate_page_max + treatment_col*treatment_page_max + after_evaluate_col*after_evaluate_page_max + adverse_event_col*adverse_event_page_max + concomitant_medication_col*concomitant_medication_page_max + follow_up_col*follow_up_page_max + 1
    matrix = [list("" for i in range(col_max)) for i in range(row_max+2)]
    for ii in range(len(patient_id)):
        patient = patient_id[ii]
        kk = 0
        
        for i in range(base_page_max):
            page = "base_" + str(i)
            sql = "SELECT name,sex,age,first_consult_date,birth_date,rt_num,patient_num,height,weight,tibiao_area,kps,ECOG FROM " + page + " WHERE patient_id='" + patient + "'"
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
            sql = "SELECT exam_date0,name0_0,name0_1,name0_2,name0_3,name0_4,name0_5,name0_6,name0_7,result0_0,result0_1,result0_2,result0_3,result0_4,result0_5,result0_6,result0_7,unit0_0,unit0_1,unit0_2,unit0_3,unit0_4,unit0_5,unit0_6,unit0_7,valuable0_0,valuable0_1,valuable0_2,valuable0_3,valuable0_4,valuable0_5,valuable0_6,valuable0_7,exam_date1,name1_0,name1_1,name1_2,name1_3,name1_4,name1_5,name1_6,name1_7,name1_8,name1_9,name1_10,name1_11,name1_12,name1_13,name1_14,name1_15,result1_0,result1_1,result1_2,result1_3,result1_4,result1_5,result1_6,result1_7,result1_8,result1_9,result1_10,result1_11,result1_12,result1_13,result1_14,result1_15,unit1_0,unit1_1,unit1_2,unit1_3,unit1_4,unit1_5,unit1_6,unit1_7,unit1_8,unit1_9,unit1_10,unit1_11,unit1_12,unit1_13,unit1_14,unit1_15,valuable1_0,valuable1_1,valuable1_2,valuable1_3,valuable1_4,valuable1_5,valuable1_6,valuable1_7,valuable1_8,valuable1_9,valuable1_10,valuable1_11,valuable1_12,valuable1_13,valuable1_14,valuable1_15,exam_date2,name2_0,name2_1,name2_2,name2_3,name2_4,name2_5,name2_6,name2_7,result2_0,result2_1,result2_2,result2_3,result2_4,result2_5,result2_6,result2_7,unit2_0,unit2_1,unit2_2,unit2_3,unit2_4,unit2_5,unit2_6,unit2_7,valuable2_0,valuable2_1,valuable2_2,valuable2_3,valuable2_4,valuable2_5,valuable2_6,valuable2_7,exam_date3,name3_0,name3_1,name3_2,name3_3,name3_4,name3_5,name3_6,name3_7,result3_0,result3_1,result3_2,result3_3,result3_4,result3_5,result3_6,result3_7,unit3_0,unit3_1,unit3_2,unit3_3,unit3_4,unit3_5,unit3_6,unit3_7,valuable3_0,valuable3_1,valuable3_2,valuable3_3,valuable3_4,valuable3_5,valuable3_6,valuable3_7,exam_date4,name4_0,name4_1,name4_2,name4_3,name4_4,name4_5,name4_6,name4_7,name4_8,name4_9,result4_0,result4_1,result4_2,result4_3,result4_4,result4_5,result4_6,result4_7,result4_8,result4_9,unit4_0,unit4_1,unit4_2,unit4_3,unit4_4,unit4_5,unit4_6,unit4_7,unit4_8,unit4_9,valuable4_0,valuable4_1,valuable4_2,valuable4_3,valuable4_4,valuable4_5,valuable4_6,valuable4_7,valuable4_8,valuable4_9,exam_date5,name5_0,name5_1,name5_2,name5_3,name5_4,name5_5,name5_6,name5_7,name5_8,name5_9,result5_0,result5_1,result5_2,result5_3,result5_4,result5_5,result5_6,result5_7,result5_8,result5_9,unit5_0,unit5_1,unit5_2,unit5_3,unit5_4,unit5_5,unit5_6,unit5_7,unit5_8,unit5_9,valuable5_0,valuable5_1,valuable5_2,valuable5_3,valuable5_4,valuable5_5,valuable5_6,valuable5_7,valuable5_8,valuable5_9,exam_date6,name6_0,name6_1,name6_2,name6_3,name6_4,name6_5,result6_0,result6_1,result6_2,result6_3,result6_4,result6_5,unit6_0,unit6_1,unit6_2,unit6_3,unit6_4,unit6_5,valuable6_0,valuable6_1,valuable6_2,valuable6_3,valuable6_4,valuable6_5 FROM " + page + " WHERE patient_id='" + patient + "'"
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
            
        for i in range(radiology_colonoscopy_page_max):
            page = "radiology_colonoscopy_" + str(i)
            sql = "SELECT chest_CT_result,chest_CT_result_other,abdomen_CT_result,abdomen_CT_result_other,pelvic_MRI_result,tumor_dist_from_anal,tumour_circle,tumor_length,can_pass,t_stage,n_stage FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(radiology_colonoscopy_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(colonoscopy_pathology_page_max):
            page = "colonoscopy_pathology_" + str(i)
            sql = "SELECT first_path_diagnose_date,pathology_type,pathology_type_other,degree_of_differentiation FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(colonoscopy_pathology_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(msi_mmr_page_max):
            page = "msi_mmr_" + str(i)
            sql = "SELECT msi_result,mmr_result FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(msi_mmr_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(gene_page_max):
            page = "gene_" + str(i)
            sql = "SELECT gene_result FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(gene_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(clinical_stage_page_max):
            page = "clinical_stage_" + str(i)
            sql = "SELECT c_t_stage,c_n_stage,c_m_stage,final_stage FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(clinical_stage_col)]
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
            
        for i in range(treatment_page_max):
            page = "treatment_" + str(i)
            sql = "SELECT group,treat_start_time,treat_end_time,treat_count,stop_reason,progress_time,dead_time FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(treatment_col)]
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
            
        for i in range(adverse_event_page_max):
            page = "adverse_event_" + str(i)
            sql = "SELECT adverse_type,start_time,end_time,nci_ctc,disposal,disposal_other,outcome,drug_relation FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(adverse_event_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(concomitant_medication_page_max):
            page = "concomitant_medication_" + str(i)
            sql = "SELECT drug,start_time,end_time,dose,method,reason FROM " + page + " WHERE patient_id='" + patient + "'"
            cur.execute(sql)
            record = []
            for row in cur:
                record = row
            if len(record)==0:
                record = ["" for j in range(concomitant_medication_col)]
            for v in record:
                kk = kk + 1
                matrix[ii+2][kk] = v
            
        for i in range(follow_up_page_max):
            page = "follow_up_" + str(i)
            sql = "SELECT follow_up_date,is_liver_metastases_resection,liver_metastases_resection_date,liver_metastases_resection_patho,is_progress,progress_date,live_state,dead_date,last_date_before_missing FROM " + page + " WHERE patient_id='" + patient + "'"
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
    
    for i in range(radiology_colonoscopy_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(radiology_colonoscopy_col_names)):
            col_name = radiology_colonoscopy_col_names[j]
            col_label = radiology_colonoscopy_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(colonoscopy_pathology_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(colonoscopy_pathology_col_names)):
            col_name = colonoscopy_pathology_col_names[j]
            col_label = colonoscopy_pathology_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(msi_mmr_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(msi_mmr_col_names)):
            col_name = msi_mmr_col_names[j]
            col_label = msi_mmr_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(gene_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(gene_col_names)):
            col_name = gene_col_names[j]
            col_label = gene_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(clinical_stage_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(clinical_stage_col_names)):
            col_name = clinical_stage_col_names[j]
            col_label = clinical_stage_col_labels[j]
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
    
    for i in range(treatment_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(treatment_col_names)):
            col_name = treatment_col_names[j]
            col_label = treatment_col_labels[j]
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
    
    for i in range(adverse_event_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(adverse_event_col_names)):
            col_name = adverse_event_col_names[j]
            col_label = adverse_event_col_labels[j]
            col_names.extend([col_name+name_suffix])
            col_labels.extend([col_label+label_suffix])
        col_names_all.extend(col_names)
        col_labels_all.extend(col_labels)
    
    for i in range(concomitant_medication_page_max):
        name_suffix = "_form"+str(i+1)
        label_suffix = "_表"+str(i+1)
        if i==0:
            name_suffix = ""
            label_suffix = ""
        col_names = []
        col_labels = []
        for j in range(len(concomitant_medication_col_names)):
            col_name = concomitant_medication_col_names[j]
            col_label = concomitant_medication_col_labels[j]
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
