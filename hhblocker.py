from os import path
from sys import platform
import shutil
import requests

class Hblocker():
    def __init__(self):
        self.urls_hosts = [
                # Adware + Malware
                # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
                # Fakenews
                # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts',
                # Gambling
                # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts',
                # Porn
                # - 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts',
                # Social media
                # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social/hosts',
                # Fakenews, gambling, porn
                'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts',
                # All
                # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts'
        ]
        self.block()

    def internet_con(self, url):
        """Internet conexion"""
        try:
            requests.get(url, timeout=1)
            return True
        except Exception as err:
            self.errors += '{} | {}\n'.format(datetime.today(), err)
            return False

    def block(self):
        if self.internet_con('https://github.com/StevenBlack/hosts'):
            if platform == 'linux':
                hosts_path = '/etc'
            elif platform == 'win32':
                hosts_path = 'C:\\Windows\\System32\\drivers\\etc'

            hosts = path.join(hosts_path, 'hosts')
            hosts_back = path.join(hosts_path, 'hosts.back')

            if not path.exists(hosts_back):
                shutil.copy(hosts, hosts_back)

            hosts_to_block = ''
            with open(hosts_back, 'r') as fback:
                hosts_to_block = fback.read()

            hosts_to_block += '\n ##Fernando Cruz UDES HOSTS BLOCKER##\n\n'
            with open(hosts, 'w') as fhosts:
                for hurl in self.urls_hosts:
                    if self.internet_con(hurl):
                        requests_hosts = requests.get(hurl)
                        requests_hosts = requests_hosts.text
                        if requests_hosts:
                            hosts_to_block += requests_hosts + '\n'
                fhosts.write(hosts_to_block)

if __name__ == '__main__':
    Hblocker()
