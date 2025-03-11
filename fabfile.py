import os
import re
import json
import subprocess
from datetime import datetime
from fabric import Connection, Config, task

# 读取服务器信息
with open("server_info.private") as server_info_text:
    server_info = json.load(server_info_text)

# 读取应用信息
with open("app_info.json") as app_info_text:
    app_info = json.load(app_info_text)

app_Name = app_info["app_name"]
version = app_info["version"]
app_dir = app_info["app_dir"]
app_dir_www = app_dir + "/www"

_REMOTE_BASE_DIR = '/home/ubuntu/web'
_TAR_FILE = "webfiles.tar.gz"

def _current_path():
    return os.path.abspath('.')

# 创建连接
conn = Connection(
    host=server_info["host"],
    user=server_info["user"],
    connect_kwargs={"password": server_info["passwd"]}
)

@task
def upload(c):
    # 删除本地旧的压缩文件
    subprocess.run('rm -f dist/webfiles.tar.gz', shell=True, check=True)
    
    # 创建新的压缩文件
    cmd = ['tar', '--dereference', '-czvf', f'dist/{_TAR_FILE}', 'crf']
    subprocess.run(cmd, check=True)
    
    # 删除远程服务器上的旧文件
    conn.run(f"rm -f {_REMOTE_BASE_DIR}/{_TAR_FILE}")
    
    # 上传新的压缩文件
    conn.put(f'dist/{_TAR_FILE}', _REMOTE_BASE_DIR)
    
    # 解压缩文件
    with conn.cd(_REMOTE_BASE_DIR):
        conn.sudo(f'tar -xzvf {_TAR_FILE}')

@task
def download(c):
    # 从远程服务器下载文件
    conn.get('/srv/MData_all/WP/www', f'{_current_path()}/download/')

@task
def deploy(c):
    # 执行远程清理脚本
    conn.run(f"bash {_REMOTE_BASE_DIR}/crf/shell/clear.sh")
    
    # 进入应用目录并执行脚本
    with conn.cd(f"{app_dir_www}/shell"):
        if version == "0":
            conn.run("bash sql.sh")
            conn.run("bash nginx.sh")
        conn.run("bash supervisor.sh")