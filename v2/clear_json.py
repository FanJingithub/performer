#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Clear json data
Date: 2020.04.08
'''

import json
import os
import shutil


if os.path.exists("clear"):
    shutil.rmtree("clear")
os.mkdir("clear")

# loading the config file
config_text = open("configuration.json",encoding="utf-8")
jsonData = config_text.read()
config_main = json.loads(jsonData)
js = json.dumps(config_main, sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)
fileName = "clear/configuration.json"
with open(fileName,"w") as coder:
    coder.write(js)


if os.path.exists("clear/configuration"):
    shutil.rmtree("clear/configuration")
os.mkdir("clear/configuration")

for config_element in config_main["elements"]:
    config_name = "configuration/config_" + config_element["name"] + ".json"
    config_text = open(config_name,encoding="utf-8")
    jsonData = config_text.read()
    config = json.loads(jsonData)
    if (config_element["name"]=="base"):
        temp = [{"class": "label","name": "patient_id","label": "ID","value": ""},
                {"class": "text","name": "name","label": "姓名","value": ""},
                {"class": "radio","name": "sex","label": "性别","count": 2,"other": 0,"options": [{"value": "男","label": "男"},{"value": "女","label": "女"}],"value": ""},
                {"class": "number","name": "age","label": "年龄","limit": [0,100],"unit": "岁","value": ""}]
    else:
        temp = [{ "class": "label","name": "patient_id","label": "ID","value": ""}]
    temp.extend(config["blocks"][0]["elements"])
    config["blocks"][0]["elements"] = temp
    js = json.dumps(config, sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)
    fileName = "clear/configuration/config_" + config_element["name"] + ".json"
    with open(fileName,"w") as coder:
        coder.write(js)

