from sys import platform

path_hosts = None
if 'linux' in platform:
    path_hosts = '/etc'
elif 'win' in platform:
    path_hosts = 'C:\Windows\System32\drivers\etc'

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
