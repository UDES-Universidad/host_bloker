#!/home/sit/miniconda3/bin/python3
#-*-coding:UTF-8-*-

from settings import path_hosts, blacklist_directories

from os import path
import shutil
import requests

hosts = path.join(path_hosts, 'host')

if path.exists(hosts):
    with open(hosts) as fhosts:
        print(fhosts.read())
else:
    print('Not exists')

txt = ''
for item in blacklist_directories:
    r = requests.get(item)
    r = r.text
    txt += r + '\n'

with open(hosts, 'w') as file_example:
    file_example.write(txt)
