#!/bin/bash

mysql -u root -p1 < ../sql/create.sql
mysql -u root -p1 < ../sql/data_status.sql

mysql -u root -p1 < ../sql/base.sql
        
mysql -u root -p1 < ../sql/physical_exam.sql
        
mysql -u root -p1 < ../sql/lab.sql
        
mysql -u root -p1 < ../sql/special_exam.sql
        
mysql -u root -p1 < ../sql/before_evaluate.sql
        
mysql -u root -p1 < ../sql/after_evaluate.sql
        