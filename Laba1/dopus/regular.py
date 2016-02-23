import re

mail = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'
    r')@(?:[A-Z0-9-]+\.)+[A-Z]{2,6}$'
    , re.IGNORECASE)

if re.findall(mail, input('text: ')):
    print(True)
else:
    print(False)


number = re.compile(r"((?<![\w.])[+-]?(?:\d+\.\d+|\d+\.|\.\d+|\d+)(?:[eE][+-]?\d+)?(?![\w.]))")
if re.findall(number, input('number :')):
    print(True)
else:
    print(False)

url_pattern = '^(?P<protocol>.*)://(?P<domen>[A-Za-z0-9\-\.]+):(?P<port>[0-9]+)?(?P<path>(/[A-z]+[^/])*)'
url = 'http://vk.com:8080/hello/world'

m = re.match(url_pattern, url)
print(m.group('protocol'))
print(m.group('domen'))
print(m.group('port'))
print(m.group('path'))

