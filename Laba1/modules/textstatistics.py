import re
from statistics import median


def text_to_list_of_words(text):
    result = []
    for item in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text):
        t = re.split(r'[\s;:\-_*\".,?!()]', item)
        t = [a for a in t if a != '']
        result.append(t)
    return result


def count_of_words(list):
    result = dict()
    for item in list:
        for i in item:
            if i in result.keys():
                result[i] += 1
            else:
                result.update({i: 1})
    return result


def average_len(lists):
    return sum([len(item) for item in lists]) / len(lists)


def median_len(lists):
    lists = sorted(lists)
    if len(lists) < 1:
        return None
    if len(lists) %2 == 1:
        return lists[((len(lists)+1)/2)-1]
    else:
        return float(sum(lists[(len(lists)/2)-1:(len(lists)/2)+1]))/2.0


def top_n_gram(lists, k=10, n=4):
    temp = dict()
    for item in lists:
        for word in item:
            for nGram in [word[i:i + n] for i in range(len(word) - n)]:
                if nGram in temp.keys():
                    temp[nGram] += 1
                else:
                    temp.update({nGram: 1})
    top = sorted(list(temp.items()), key=lambda elem: elem[1], reverse=True)
    if not len(top) > k:
        return [a[0] for a in top]
    else:
        return [a[0] for a in top[:k]]
