#!/bin/bash

sed -i.bak '/res = \[self.patient_id/ {
  r lab_default.txt
  d
}' ../handlers/api_labHandler.py

sed -i.bak 's|256|16|g' ../sql/lab.sql
sed -i.bak '/result/s/16/6/' ../sql/lab.sql
sed -i.bak '/unit/s/16/8/' ../sql/lab.sql
sed -i.bak '/valuable/s/16/4/' ../sql/lab.sql
