#!/home/sit/miniconda3/envs/blocker/bin/python3
# -*-coding:UTF-8-*-

from settings import path_hosts, blacklist_directories, logs_file, reference
from datetime import datetime
from os import path, getcwd
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
            self.errors += '{} | {}\n'.format(datetime.today(), err)
            return False

    def logs(self):
        txt = ''
        if path.exists(logs_file):
            txt = open(logs_file, 'r')
            txt = txt.read()

        if self.errors:
            with open(logs_file, 'w') as new_errors:
                new_errors.write('-> {}\n{}'.format(self.errors, txt))
        else:
            with open(logs_file, 'w') as new_errors:
                new_errors.write('-> {} Last correct update.\n{}'.format(datetime.today(), txt))

    def check_file(self):
        hosts_path = path.join(path_hosts, 'hosts')
        hosts_data = ''
        date_update = ''
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

                    with open(path.join(path_hosts, 'hosts'), 'r') as lhosts:
                        lines = lhosts.readlines()
                        for line in lines:
                            if 'Date:' in line:
                                date_update = line

        else:
            with open(hosts_path, 'w') as new_file_hosts:
                new_file_hosts.write('##HOSTS##')

        return (date_update, hosts_path, hosts_data)

    def block(self):
        if self.internet_con('https://github.com'):
            date_update, hosts_path, hosts_data = self.check_file()

            hosts_data += '\n' + len(reference) * '#' + '\n'
            hosts_data += reference
            hosts_data += '\n' + len(reference) * '#' + '\n'
            hosts_data += '\nLast update: {}\n\n'.format(datetime.today())

            hosts_to_block = ''
            for item in blacklist_directories:
                if self.internet_con(item):
                    requests_hosts = requests.get(item)
                    requests_hosts = requests_hosts.text
                    if requests_hosts:
                        if not date_update or date_update not in requests_hosts:
                            hosts_to_block += requests_hosts + '\n'

            if hosts_to_block:
                with open(hosts_path, 'w') as whosts:
                    whosts.write(hosts_data + hosts_to_block)
                self.logs()

if __name__ == '__main__':
    b = Blocker()
    # print(b.check_file())
