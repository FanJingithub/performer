#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Fan Jin'

'''
Deployment toolkit.
'''

import os, re

from datetime import datetime
from fabric.api import *
import json

server_info_text = open("server_info.private")
jsonData = server_info_text.read()
server_info = json.loads(jsonData)

env.hosts = [server_info["host"]]
env.user = server_info["user"]
env.sudo_user = server_info["user"]
env.password = server_info["passwd"]

app_Name = "Test"
version = "1"
app_dir = "/srv/MData_all/Test"
app_dir_www = "/srv/MData_all/Test/www"

_REMOTE_BASE_DIR = '/home/ubuntu/files/Web'
_TAR_FILE = "webfiles.tar.gz"

def _current_path():
    return os.path.abspath('.')

def upload():
    local('rm -f dist/webfiles.tar.gz')
    cmd = ['tar', '--dereference', '-czvf', 'dist/%s v2' % _TAR_FILE]
    local(' '.join(cmd))
    run("rm -f %s/%s" % (_REMOTE_BASE_DIR, _TAR_FILE))
    put('dist/%s' % _TAR_FILE, _REMOTE_BASE_DIR)
    with cd(_REMOTE_BASE_DIR):
        sudo('tar -xzvf %s' % _TAR_FILE)

def download():
    get('/srv/MData_all/WP/www','%s/download/' % _current_path())

def deploy():
    run("bash %s/v2/shell/clear.sh" % _REMOTE_BASE_DIR)
    with cd("%s/shell" % app_dir_www):
        if version=="0":
            run("bash sql.sh")
            run("bash nginx.sh")
        run("bash supervisor.sh")
