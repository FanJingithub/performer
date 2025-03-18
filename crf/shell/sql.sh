#!/bin/bash

mysql -u root -p1 < ../sql/create.sql
mysql -u root -p1 < ../sql/data_status.sql

mysql -u root -p1 < ../sql/base.sql
        
mysql -u root -p1 < ../sql/physical_exam.sql
        
mysql -u root -p1 < ../sql/lab.sql
        
mysql -u root -p1 < ../sql/special_exam.sql
        
mysql -u root -p1 < ../sql/radiology_colonoscopy.sql
        
mysql -u root -p1 < ../sql/colonoscopy_pathology.sql
        
mysql -u root -p1 < ../sql/msi_mmr.sql
        
mysql -u root -p1 < ../sql/gene.sql
        
mysql -u root -p1 < ../sql/clinical_stage.sql
        
mysql -u root -p1 < ../sql/before_evaluate.sql
        
mysql -u root -p1 < ../sql/treatment.sql
        
mysql -u root -p1 < ../sql/after_evaluate.sql
        
mysql -u root -p1 < ../sql/adverse_event.sql
        
mysql -u root -p1 < ../sql/concomitant_medication.sql
        
mysql -u root -p1 < ../sql/follow_up.sql
        