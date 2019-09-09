#!/home/sit/miniconda3/bin/python3
#-*-coding:UTF-8-*-

from settings import path_hosts, blacklist_directories
from datetime import datetime
from os import path
import shutil
import requests

hosts_path = path.join(path_hosts, 'hosts')
reference = '##BlockerUDES##'

hosts_data = ''
if path.exists(hosts_path):
    with open(hosts_path, 'r') as fhosts:
        lines = fhosts.readlines()
        exist_reference = False
        if reference+'\n' in lines:
            exist_reference = True

        if not exist_reference:
            shutil.copy(hosts_path, path.join(path_hosts, 'hosts.back'))
            with open(hosts_path, 'r') as rhosts:
                hosts_data = rhosts.read()
        else:
            with open(path.join(path_hosts, 'hosts.back'), 'r') as rhosts:
                hosts_data = rhosts.read()



    with open(hosts_path, 'w') as whosts:
        hosts_data += '\n' + len(reference) * '#' + '\n'
        hosts_data += reference
        hosts_data += '\n' + len(reference) * '#' + '\n'
        hosts_data += '\nLast update: {}\n\n'.format(datetime.today())
        for item in blacklist_directories:
            r = requests.get(item)
            r = r.text
            hosts_data += r + '\n'
            whosts.write(hosts_data)
