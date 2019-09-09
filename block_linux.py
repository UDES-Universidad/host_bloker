import shutil
import requests

#Path to the host file
host_path_base = '/etc/hosts.bak'
host_path_exec = '/etc/hosts'
blacklistURLs = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts'
    #'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/social/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-porn/hosts',
    #'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-social/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn/hosts',
    #'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-social/hosts',
    #'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn-social/hosts',
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts',
    #'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-social/hosts',
    # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-porn-social/hosts',
    # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn-social/hosts',
    # 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts'
    ]

# Get the base text for a hosts file
def txtBase():
    with open(host_path_base, 'r') as base:
        sites = ''
        lines = base.readlines()
        for l in lines:
            sites += l
        return sites + '\n'

# Get hosts from text
def stringParser(txt):
    txt = txt.split('\n')
    newtxt = ''
    for t in txt:
        if t.startswith('0.0.0.0'):
            r = t.split(' ')[1]
            if r != '0.0.0.0':
                newtxt += t + '\n'
    return newtxt

# Get text from hosts servers
def getsites(url):
    try:
        r = requests.get(url)
        return r.text
    except Exception as e:
        print('Error: {}'.format(e))

# Generate the file with the content to block
def generateBlockFile(arr):
    body = txtBase()
    for i in arr:
        body += stringParser(getsites(i))
    with open(host_path_exec, 'w') as f:
        f.write(body)


if __name__ == '__main__':
    print(generateBlockFile(blacklistURLs))
