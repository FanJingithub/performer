#!/bin/bash

mysql -u root -p1 < ../sql/create.sql
mysql -u root -p1 < ../sql/data_status.sql

mysql -u root -p1 < ../sql/base.sql
        
mysql -u root -p1 < ../sql/lab.sql
        
mysql -u root -p1 < ../sql/pathology.sql
        
mysql -u root -p1 < ../sql/surgery.sql
        
mysql -u root -p1 < ../sql/chemotherapy.sql
        
mysql -u root -p1 < ../sql/radiotherapy.sql
        
mysql -u root -p1 < ../sql/follow_up.sql
        