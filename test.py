from sys import platform
import yaml

data = yaml.load(open('db.yaml', 'r'), Loader=yaml.FullLoader)

print(data['os'][platform])
