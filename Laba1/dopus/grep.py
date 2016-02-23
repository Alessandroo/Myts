import re


def grep(repository, pattern):
    print(pattern)
    for item in repository:
        found = re.findall(pattern, str(item))
        if len(found) > 0 and found[0] == item:
            print(item)


a = set(['123', '45646', '54654', '897654', '44', 'asd'])

for i in '120':
    print(i)
