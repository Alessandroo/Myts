def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


def merge_sort(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
    return lst
