def merge(left, right, reverse=False):
    result = []
    while left and right:
        if left[0] < right[0]:
            if not reverse:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        else:
            if not reverse:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


def merge_sort(lst, reverse=False):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(merge_sort(lst[:mid], reverse), merge_sort(lst[mid:], reverse), reverse)
    return lst

if __name__ == '__main__':
    array = [x for x in range(10)]
    print(merge_sort(array))