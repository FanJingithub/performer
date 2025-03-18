
name = [[] for i in range(7)]
name[0] = ["白细胞计数 WBC", "红细胞计数 RBC", "血红蛋白 Hb", "血小板计数 PLT", "中性粒细胞 NEU"]
name[1] = ["总胆红素 TB", "直接胆红素 STB", "谷草转氨酶 AST", "谷丙转氨酶 ALT", "血清碱性磷酸酶 ALP", "血尿素氮 BUN", "血肌酐 Cr", "血糖 GLU", "血尿素 UA"]
name[2] = ["钾 K", "钠 Na", "氯 Cl", "钙 Ca", "磷 P"]
name[3] = ["癌胚抗原 CEA", "甲胎蛋白 AFP", "糖类抗原50 CA50", "糖类抗原199 CA199", "糖类抗原724 CA724", "糖类抗原242 CA242"]
name[4] = ["游离三碘甲状腺素 FT3", "游离甲状腺激素 FT4", "促甲状腺素 TSH", "甲状腺球蛋白 HTG", "甲状腺球蛋白抗体 TGAb", "抗甲状腺过氧化物酶 TPOAb", "降钙素 CT"]
name[5] = ["促肾上腺皮质激素 ACTH", "皮质醇 COR", "促黄体生成素 LH", "卵泡刺激素 FSH", "泌乳素 PRL", "孕酮 ProGES", "雌二醇 E2", "睾酮 T"]
name[6] = ["肌酸激酶同工酶 CKMB", "超敏肌钙蛋白 cTnT", "B型利钠肽前体 ProBNP", "肌红蛋白"]

unit = [[] for i in range(7)]
unit[0] = ["10^9/L", "10^12/L", "g/L", "10^9/L", "10^9/L"]
unit[1] = ["mol/L", "umol/L", "U/L", "U/L", "U/L", "mmol/L", "mol/L", "mmol/L", "umol/L"]
unit[2] = ["mmol/L", "mmol/L", "mmol/L", "mmol/L", "mmol/L"]
unit[3] = ["ug/L", "ug/L", "U/L", "U/L", "U/L", "U/L"]
unit[4] = ["pmol/L", "pmol/L", "mIU/L", "ng/ml", "IU/ml", "pg/ml"]
unit[5] = ["pmol/L", "pmol/L", "IU/L", "IU/L", "mIU/L", "nmol/L", "pmol/L", "nmol/L"]
unit[6] = ["ng/mL", "ng/mL", "pmol/L", "ng/mL"]

import json
config_text = open("../clear/configuration/config_lab.json",encoding="utf-8")
jsonData = config_text.read()
config = json.loads(jsonData)

output = open("lab_default.txt",'w')
first_line = "        res = [self.patient_id, \n"
output.write(first_line)

for i in range(len(config['blocks'])):
    block = config['blocks'][i]
    for element in block['elements']:
        if element['class'] == 'table':
            rows = int(element['row'])
            print(rows)
            part = [""] + name[i] +  [""]*(2*rows - len(name[i])) + unit[i] + [""]*(2*rows - len(unit[i]))
            line = '        "' + '","'.join(part) + '"'
            if i < len(config['blocks']) - 1:
                line += ",\n"
            output.write(line)

output.write("]\n")