from modules.textstatistics import count_of_words, text_to_list_of_words, top_n_gram, median_len, average_len

print('Task 1.1')
while True:
    print('1. Enter text')
    print('2. Open from file')
    user_input = input('Menu 1: ')
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
    print('1. Numbers of repeats of the words ')
    print('2. Average count of words in sentence ')
    print('3. Median count of words in sentence ')
    print('4. Top K words N-gram')
    print('5. Exit')
    user_input = input('Menu 2: ')

    try:
        user_input = int(user_input)
    except ValueError:
        print('Incorrect input')
        continue

    if user_input == 1:
        for p, v in count_of_words(text).items():
            print('{0} : {1}'.format(p, v))
        print()
    elif user_input == 2:
        print(average_len(text_to_list_of_words(text)))
        print()
    elif user_input == 3:
        print(median_len(text_to_list_of_words(text)))
        print()
    elif user_input == 4:
        try:
            k = int(input('Input k for top k-words '))
            n = int(input('Input n for n-grams '))
            for item in top_n_gram(text_to_list_of_words(text), k, n):
                print(item, end=' ')
            print()
        except ValueError:
            for item in top_n_gram(text_to_list_of_words(text)):
                print(item, end=' ')
        print()
    elif user_input == 5:
        break
    else:
        print('Incorrect input')