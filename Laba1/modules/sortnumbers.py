import re


def sort(text, func):
    return func(list(map(int, re.findall(r'\d+', text))))
