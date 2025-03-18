#!/bin/bash

sed -i.bak '/res = \[self.patient_id/ {
  r after_evaluate_default.txt
  d
}' ../handlers/api_after_evaluateHandler.py


sed -i.bak '/res = \[self.patient_id/ {
  r before_evaluate_default.txt
  d
}' ../handlers/api_before_evaluateHandler.py
