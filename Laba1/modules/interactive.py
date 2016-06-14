import re


# All methods made have two or more parameters for correct work

class Interactive:
    def __init__(self):
        self.repository = set()

    def add(self, *items):
        print(items)
        self.repository.update(*items)

    def remove(self, *item):
        if item[0]:
            self.repository.discard(*item)

    def find(self, *items):
        for item in self.repository.intersection(*items):
            print(item, end=' ')
        print()

    def list(self, *other):
        for item in self.repository:
            print(item, end=' ')
        print()

    def load(self, *other):
        filename = other[0].pop()
        try:
            with open(filename) as file:
                self.repository.update(line.strip() for line in file)
        except FileNotFoundError:
            print('File not found')

    def save(self, *other):
        filename = other[0].pop()
        try:
            with open(filename, 'w+') as file:
                for index in self.repository:
                    file.write(index + '\n')
        except FileNotFoundError:
            print('File not found')

    def clear(self, *other):
        self.repository.clear()

    def grep(self, *other):
        pattern = other[0].pop()
        for item in self.repository:
            found = re.findall(pattern, item)
            if len(found) > 0 and found[0] == item:
                print(item, end=' ')
        print()


def writen():
    inter = Interactive()
    text = input('Wild: ').split(' ')
    while text[0] != 'exit':
        if text[0] in filter(lambda arg: getattr(Interactive, arg), dir(Interactive)):
            try:
                getattr(inter, text[0])(text[1:])
            except AttributeError:
                print('Incorrect Input')
        else:
            print('function ' + text[0] + ' isn\'t find')
        text = input('Wild: ').split(' ')
