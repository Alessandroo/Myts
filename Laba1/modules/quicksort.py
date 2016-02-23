import random


def quick_sort(lists):
    if lists:
        pivot = lists[random.choice(range(0, len(lists)))]
        return quick_sort([x for x in lists if x < pivot]) + \
               [x for x in lists if x == pivot] + \
               quick_sort([x for x in lists if x > pivot])
    return []
