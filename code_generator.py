#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Web Frame: performer (An automatic full-stack web frame, which can generate numerous form-style web pages with backend code)
File Name: code_generator
Description: The HTML, Javascript, and Python Code can be generated by the code_generator
Author: Fan Jin
Date: 2019.05.11
'''

import json

# generator the HTML code
def generateHTML(editable):

    # generator the Javascript code
    def generateJS(editable):
        
        if (editable==0):
            #-------------------------------------------------------------
            # read version
            #typeName = "read"
            code =  '''var vm = new Vue({
            el: '#vm',
            data: {'''
            for i in range(len(config["elements"])):
                element = config["elements"][i]
                newCode = '''
                {0}: "{{{{{0}}}}}" '''.format(element["name"])
                code = code + newCode
                if (i<len(config["elements"])-1):
                    code = code + ","
                else:
                    code = code + '''
            }},
            methods:{{
                submit:function(){{
                    return 0;
                }},
                edit:function(){{
                    window.location.href="/{0}?patient_id={{{{patient_id}}}}&edit=1";
                }}
            }}
        }});'''.format(configName)
            #------------------------------------------------------------
        else:
            #-------------------------------------------------------------
            # edit version
            #typeName = "edit"
            code = '''var vm = new Vue({
            el: '#vm',
            data: {'''
            for i in range(len(config["elements"])):
                element = config["elements"][i]
                newCode = '''
                {0}: "{{{{{0}}}}}" '''.format(element["name"])
                code = code + newCode
                if (i<len(config["elements"])-1):
                    code = code + ","
                else:
                    code = code + '''
            }},
            mounted(){{
                this.init()
            }},
            methods:{{
                init:function(){{
                this.$http.get('/api/{0}?patient_id={{{{patient_id}}}}').then(function(res){{'''.format(configName)
            
            for i in range(len(config["elements"])):
                element = config["elements"][i]
                newCode = '''
                    this.{0}=res.data.{0};'''.format(element["name"])
                code = code + newCode

            code = code + '''
                },function(){
                    console.log('error');
                });
                },
                submit: function(event) {
                    event.preventDefault();
                    var
                    $form = $('#vm'),
                    data = {'''

            for i in range(len(config["elements"])):
                element = config["elements"][i]
                newCode = '''
                        {0}: this.{0}'''.format(element["name"])
                code = code + newCode
                if (i<len(config["elements"])-1):
                    code = code + ","
                else:
                    code = code + '''
                    };'''

            code = code + '''
                    this.$http.post('/{0}',data,{{emulateJSON:true}}).then(function(res){{
                        document.write(res.body);    
                    }},function(res){{
                        console.log(res.status);
                    }});
                }}
            }}
        }});'''.format(configName)
            #------------------------------------------------------------

        #fileName = "./js/"+typeName + "_" +configName + "_code.js"
        #with open(fileName,"w") as coder:
        #    coder.write(code)
        return code

    # --------------------------------------
    # the main code for generating HTML code
    disabled = ""
    #buttonName = "提交"
    #buttonAction = ''
    typeName = "edit"
    if (editable==0):
        disabled = "disabled"
        #buttonName = "编辑"
        #buttonAction = ''' v-on:click="/{0}?patient_id={{{{patient_id}}}}&edit=1" '''.format(configName)
        typeName = "read"

    code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Data System</title>
    <link rel="stylesheet" href="css/style.css">
    <script src="./js/vue.js"></script>
    <script src="./js/vue-resource.js"></script>
    <script src="./js/jquery-3.4.1.js"></script>
</head>
<body>
    <div class="main-body">
        <div class="heading">
            <h1>临床科研数据库系统</h1>
        </div>
        <div id="menu" class="menu">
            <div style="text-align:center">
                <h3>导航栏</h3>
            </div>'''

    code = code + '''
            <div class="menu-item">
                <a class="item-link" href="/list">
                    <div>病例列表</div>
                </a>
            </div>
            '''
    for i in range(len(config_main["elements"])):
        element = config_main["elements"][i]
        code = code + '''
            <div class="menu-item">
                <a class="item-link" href="/{0}?patient_id={{{{patient_id}}}}">
                    <div>{1}</div>
                </a>
            </div>'''.format(element["name"], element["label"])
    code = code + '''
        </div>
        <div class="container">
            <div style="text-align:center">
                <h2>{0}</h2>
            </div>
            <br>
            <form id="vm" v-on:submit="submit">
                <input type="text" value="{{{{patient_id}}}}" v-model="patient_id" v-show="false"></input>
                <div class="form-part-1">'''.format(config["label"])


    len_elements = len(config["elements"])
    len_half = (len_elements) // 2 + 1

    for i in range(0,len_elements):
        if (i==len_half):
            code = code + '''
                </div>
                <div class="form-part-2">'''

        element = config["elements"][i]
        newCode = ""
        if (element["class"]=="label"):
            pass
        elif (element["class"]=="text"):
            newCode = '''
                    <div>
                        <label class="form-label">{0}: </label>
                        <input class="form-text" v-model="{1}" {2}>
                        <br><br>
                    </div>'''.format(element["label"], element["name"], disabled)
        
        elif (element["class"]=="number"):
            newCode = '''
                    <div>
                        <label class="form-label">{0}: </label>
                        <input class="form-number" type="number" v-model.number="{1}" {3}>
                        <label>&nbsp;{2}</label>
                        <br><br>
                    </div>'''.format(element["label"], element["name"], element["unit"], disabled)

        elif (element["class"]=="radio"):
            newCode = '''
                    <div>
                        <label class="form-label">{0}: </label>
                        <br>'''.format(element["label"])
            for j in range(len(element["options"])):
                newOption = '''
                        <input class="form-radio" type="radio" id="{0}" value="{0}" v-model="{2}" {3}>
                        <label for="{0}">{1}</label>
                        <br>'''.format(element["options"][j]["value"], element["options"][j]["label"], element["name"], disabled)
                newCode = newCode + newOption
            newCode = newCode + '''<br>
                    </div>'''
            
        elif (element["class"]=="time"):
            pass
        elif (element["class"]=="select"):
            pass
        code = code + newCode

    if (editable==1):
        newCode = '''</div>
                <div class="form-part-3">
                    <input type="submit" value="提交">
                </div>    
            </form>
        </div>
    </div>
    <script>
        '''
    else:
        newCode = '''</div>
                <div class="form-part-3">
                    <button class="submit" type="button" v-on:click="edit">编辑</button>
                </div>    
            </form>
        </div>
    </div>
    <script>
        '''.format(configName)
    code = code + newCode

    code = code + generateJS(editable)

    code = code + '''
    </script>
</body>
</html>'''

    fileName = "html/" + typeName + "_" +configName + "_page.html"
    with open(fileName,"w") as coder:
        coder.write(code)

# generator the Python Handler:
def generatePython_Handler():

    # ==========================
    # generator the page Handler
    code = '''# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class ''' 
    code = code + configName +"Handler(tornado.web.RequestHandler):"

    # -----------------------
    # generate the GET method
    code = code + '''

    def get(self):
        print('----------------------------Get {0}--------------------------')

        try:
            edit = self.get_argument("edit", "0")
        except:
            edit = "0"
        
        self.patient_id = self.get_argument("patient_id", "")
        exist = 0
        
        # Get the patient's data status from the database
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        self.cur = conn.cursor()
        self.cur.execute('''.format(configName)
    code = code + "'''" + "SELECT " + configName + " FROM data_status WHERE patient_id='{0}' " + "'''"
    code = code + '''.format(self.patient_id))
        for row in self.cur:
            exist = row[0]
        self.cur.close()'''
    
    # generate the dynamic part for GET methon
    part_1 = ""
    part_2 = ' patient_id=self.patient_id '
    part_3 = ""
    k = 0
    for i in range(len(config["elements"])):
        element = config["elements"][i]
        part_1 = part_1 + element["name"]
        if (element["class"]!="label"):
            part_2 = part_2 + ''' {0}=res[{1}]'''.format(element["name"],k)
        if (i<len(config["elements"])-1):
            part_1 = part_1 + ","
            part_2 = part_2 + ","
            part_3 = part_3 + ', ""'
        else:
            part_1 = part_1 + " FROM "
        k = k + 1

    code = code + '''

        res = ['''
    code = code + "self.patient_id" + part_3 +"]"

    code =code + '''

        if (exist==1):
            # Get the data from the database
            self.cur = conn.cursor()
            self.cur.execute('''
    code = code + "'''SELECT "

    code = code + part_1 + configName + " WHERE patient_id='{0}' '''.format(self.patient_id))"
    code = code + '''
            for row in self.cur:
                res = row'''
    code = code + '''

        if (exist==1 and edit=="0"):
            self.render("../html/read_'''
    code = code + configName + '''_page.html",''' + part_2 + ''')
        else:
            self.render("../html/edit_'''
    code = code + configName + '''_page.html",''' + part_2 + ''')'''

    # ------------------------
    # generate the POST method
    code = code + '''

    def post(self):
        print('----------------------------Submit----------------------------')

        self.patient_id = self.get_body_argument("patient_id")
        '''
    # generate the dynamic part for POST method
    part_0 = ""
    part_1_1 = "patient_id, "
    part_1_2 = "'{0}', "
    part_2 = "self.patient_id, "
    part_3 = ' patient_id=self.patient_id, '
    k = 0
    for i in range(len(config["elements"])):
        element = config["elements"][i]
        if (element["class"]=="label"):
            continue
        part_0 = part_0 + element["name"] + ' = self.get_body_argument("'+ element["name"] + '") ' + '''
        '''
        part_1_1 = part_1_1 + element["name"]
        part_1_2 = part_1_2 + "'{" + str(i) + "}'"
        part_2 = part_2 + element["name"]
        part_3 = part_3 +  element["name"] + '=' + element["name"]
        if (i<len(config["elements"])-1):
            part_1_1 = part_1_1 + ", "
            part_1_2 = part_1_2 + ", "
            part_2 = part_2 + ","
            part_3 = part_3 + ", "
        k = k + 1

    code = code + part_0 + '''
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)

        # Insert the data into the database
        self.cur = conn.cursor()
        '''
    code = code + "sqls = '''REPLACE INTO " + configName + " "

    code = code + "(" + part_1_1 + ") VALUES (" + part_1_2 + ")" + " '''.format(" + part_2 + ")"
    code = code + '''
        self.cur.execute(sqls)

        sqls = "SELECT * FROM data_status WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        exist_data = 0
        for row in self.cur:
            exist_data = row
            exist_data = 1
        
        if (exist_data == 1):
            sqls = "UPDATE data_status SET {0}=1 WHERE patient_id='" + self.patient_id + "'"
        else:
            sqls = "REPLACE INTO data_status (patient_id,{0}) VALUES ('"+ self.patient_id + "'," + "1)"

        self.cur.execute(sqls)
        self.cur.close()'''.format(configName)
    
    code = code + '''

        self.render("../html/read_'''
    code = code + configName + '''_page.html",''' + part_3 + ''')
'''

    fileName = "./handlers/" + configName + "Handler.py"
    with open(fileName,"w") as coder:
        coder.write(code)

    # ==========================
    # generator the api Handler
    code = '''# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os, MySQLdb
import tornado.gen
import tornado.web
import json

class api_''' 
    code = code + configName +"Handler(tornado.web.RequestHandler):"
    code = code + '''

    def get(self):
        print('----------------------------Get api-{0}----------------------')
        self.patient_id = self.get_argument("patient_id", "")'''.format(configName)
    
    code = code + '''
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        self.cur.execute('''
    code = code + "'''SELECT "
    # generate the dynamic part for api Handler
    part_1 = ""
    part_2 = ' "patient_id":self.patient_id'
    part_3 = ""
    for i in range(len(config["elements"])):
        element = config["elements"][i]
        part_1 = part_1 + element["name"]
        if (element["class"]!="label"):
            part_2 = part_2 + ''' "{0}":res[{1}]'''.format(element["name"],i)
        if (i<len(config["elements"])-1):
            part_1 = part_1 + ","
            part_2 = part_2 + ","
            part_3 = part_3 + ', ""'
        else:
            part_1 = part_1 + " FROM "
            part_2 = part_2 + "}"
    
    code = code + part_1 + configName + " WHERE patient_id='{0}' '''.format(self.patient_id))"
    code = code + '''
        res = ['''
    code = code + "self.patient_id" + part_3 +"]"
    code = code + '''
        for row in self.cur:
            res = row
        self.data = {'''
    code = code + part_2
    code = code + '''
        self.write(json.dumps(self.data))
'''

    fileName = "./handlers/api_" + configName + "Handler.py"
    with open(fileName,"w") as coder:
        coder.write(code)
    
# generator the SQL code: Handler
def generateSQL_Handler():
    code = '''use MData;

grant select, insert, update, delete on MData.* to 'fanjin'@'localhost' identified by 'fmvKL0UlQ558lKWG';

'''

    code = code + "create table " + configName + " ("
    code = code + '''
    '''
    for i in range(len(config["elements"])):
        element = config["elements"][i]
        code = code + "`" + element["name"] + "`  varchar(12) default ''"
        code = code + ''',
    '''
    code = code + '''primary key(patient_id)
) engine=innodb         default charset=utf8;
'''

    fileName = "./sql/" + configName + ".sql"
    with open(fileName,"w") as coder:
        coder.write(code)

# generator the SQL code: TABLE data_status
def generateSQL_dataStatus():
    code = '''use MData;

grant select, insert, update, delete on MData.* to 'fanjin'@'localhost' identified by 'fmvKL0UlQ558lKWG';

'''

    code = code + "create table data_status ("
    code = code + '''
    `patient_id`  varchar(12)  default '',
    '''
    for i in range(len(config_main["elements"])):
        element = config_main["elements"][i]
        code = code + "`" + element["name"] + "`  INT default 0"
        if (i<len(config_main["elements"])-1):
            code = code + ''',
    '''
        else:
            code = code + '''
) engine=innodb         default charset=utf8;
'''

    fileName = "./sql/data_status.sql"
    with open(fileName,"w") as coder:
        coder.write(code)

# generator the Python App.py:
def generatePython_App():

    code = '''# -*- coding:utf-8 -*-
# Created by Machine (Fan Jin build the code-generator)

import tornado, os
import tornado.web
from tornado import netutil, process, httpserver
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

import MySQLdb

import json

'''

    part_1 = ""
    part_2 = ""
    part_3 = '''("/list",      listHandler),
                        ("/api/new",      api_newHandler),
                        ("/api/list",      api_listHandler),
                        '''
    part_4 = ""
    for i in range(len(config_main["elements"])):
        element = config_main["elements"][i]
        part_1 = part_1 + "from handlers." + element["name"] + "Handler import " + element["name"] + "Handler" + '''
'''
        part_2 = part_2 + "from handlers.api_" + element["name"] + "Handler import api_" + element["name"] + "Handler" + '''
'''
        part_3 = part_3 + '("/' + element["name"] + '",      ' + element["name"] + "Handler)" + ''',
                        '''
        part_4 = part_4 + '("/api/' + element["name"] + '",      api_' + element["name"] + "Handler)"
        if (i<len(config_main["elements"])-1):
            part_4 = part_4 + ''',
                        '''
    
    code = code + part_1 +part_2

    code = code + '''
class listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get list--------------------------')
        self.render("list.html")

class api_newHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get new--------------------------')
        self.patient_id = self.get_argument("patient_id", "")
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id FROM base WHERE patient_id='" + self.patient_id + "'"
        self.cur.execute(sqls)
        result = 0
        for row in self.cur:
            result = 1
        self.data = { "patient_id": self.patient_id, "result": result }
        self.write(json.dumps(self.data))

class api_listHandler(tornado.web.RequestHandler):

    def get(self):
        print('----------------------------Get api-list--------------------------')
        conn = MySQLdb.connect( host   = 'localhost',
                                user   = 'debian-sys-maint',
                                passwd = 'fmvKL0UlQ558lKWG',
                                db     = 'MData',
                                charset= 'utf8')
        conn.autocommit(1)
        # Get the data from the database
        self.cur = conn.cursor()
        sqls = "SELECT patient_id,sex,age FROM base"
        self.cur.execute(sqls)
        patient_list = []
        for row in self.cur:
            patient_list.append({
                "patient_id": row[0],
                "sex": row[1],
                "age": row[2]
            })
        print(patient_list)
        self.write(json.dumps(patient_list))
'''

    code = code + '''

class Application(tornado.web.Application):

    def __init__(self):

        handlers =  [
                        '''
    code = code + part_3 + part_4

    code = code + '''
                    ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    app = Application()
    print('----------------------------Start Server----------------------------')
    server = HTTPServer(app)
    server.listen(6002)
    IOLoop.current().start()
'''

    fileName = "app.py"
    with open(fileName,"w") as coder:
        coder.write(code)


# loading the config file
config_text = open("configuration.json")
jsonData = config_text.read()
config_main = json.loads(jsonData)

# test the loading file
print("-------------------Check the main configuration File---------------------")
print(config_main["elements"][0])
print("-------------------------------------------------------------------------")

for config_element in config_main["elements"]:
    config_name = "configuration/config_" + config_element["name"] + ".json"
    config_text = open(config_name)
    jsonData = config_text.read()
    config = json.loads(jsonData)
    configName = config["name"]

    # test the loading file
    print("--------------------------Test the Loading File--------------------------")
    print(config["elements"][1])
    print("-------------------------------------------------------------------------")

    generateHTML(0)
    generateHTML(1)
    generatePython_Handler()
    generateSQL_Handler()

generateSQL_dataStatus()
generatePython_App()
