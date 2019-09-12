from sys import platform

path_hosts = None
# Errors path file
logs_file = ''
if 'linux' in platform:
    path_hosts = '/etc'
    logs_file = '/home/sit/Documentos/python/logs.txt'
elif 'win' in platform:
    path_hosts = 'C:\\Windows\\System32\\drivers\\etc'
    logs_file = 'C:\\Users\\Administrador\\Documents\\logs.txt'

blacklist_directories = [
# Adware + Malware
# 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
# Fakenews
# 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts',
# Gambling
# 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts',
# Porn
# 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts',
# Social media
# 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social/hosts',
# Fakenews, gambling, porn
'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts',
# All
# 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts'
]

hosts_extras = [
    ''
]

reference = '##BlockerUDES##'
