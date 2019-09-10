#!/home/sit/miniconda3/envs/blocker/bin/python3
# -*-coding:UTF-8-*-

from settings import path_hosts, blacklist_directories
from datetime import datetime
from os import path
import shutil
import requests

class Blocker:
    def __init__(self):
        self.errors = ''
        self.block()

    def internet_con(self, url):
        try:
            requests.get(url, timeout=1)
            return True
        except Exception as err:
            self.errors = '{}\n'.format(err)
            return False

    def block(self):
        if self.internet_con('https://github.com'):
            hosts_path = path.join(path_hosts, 'hosts')
            reference = '##BlockerUDES##'

            hosts_data = ''
            if path.exists(hosts_path):
                with open(hosts_path, 'r') as fhosts:
                    txt_raw = fhosts.read()
                    if reference not in txt_raw:
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
                        if self.internet_con(item):
                            r = requests.get(item)
                            r = r.text
                            hosts_data += r + '\n'
                            whosts.write(hosts_data)

if __name__ == '__main__':
    b = Blocker()
    print(b.errors)
