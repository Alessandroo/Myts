from modules.quicksort import quick_sort
from modules.mergesort import merge_sort
from modules.radixsort import radix_sort
from modules.sortnumbers import sort


def write_sorted_list(list):
    for item in list:
        print(item, end=',')

print('Task 1.2')

while True:
    print('1. Enter text')
    print('2. Open from file')
    user_input = input()
    try:
        user_input = int(user_input)
    except ValueError:
        print('Incorrect input')
    if user_input == 1:
        try:
            text = input('Input text: ')
        except ValueError:
            print('Incorrect input')
        break
    elif user_input == 2:
        filename = input()
        try:
            with open(filename) as file:
                text = file.read()
            break
        except FileNotFoundError:
            print('File not found')
    else:
        print('Incorrect input')

print()

while True:
    print('1. Quick Sort')
    print('2. Merge Sort')
    print('3. Radix Sort')
    print('4. Exit')
    user_input = input()

    try:
        user_input = int(user_input)
    except ValueError:
        print('Incorrect input')
        continue

    if user_input == 1:
        write_sorted_list(sort(text, quick_sort))
        print()
    elif user_input == 2:
        write_sorted_list(sort(text, merge_sort))
        print()
    elif user_input == 3:
        write_sorted_list(sort(text, radix_sort))
        print()
    elif user_input == 4:
        break
    else:
        print('Incorrect input')
