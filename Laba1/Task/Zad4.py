from modules.fibo import fibo

print('Task 1.4')

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
            number = int(input('Input text: '))
        except ValueError:
            print('Incorrect input')
        break
    elif user_input == 2:
        filename = input()
        try:
            with open(filename) as file:
                number = int(file.read())
            break
        except FileNotFoundError:
            print('File not found')
        except ValueError:
            print('File has incorrect data')
    else:
        print('Incorrect input')

print()

while True:
    print('1. Calculate Fibo Numbers')
    print('2. Exit')
    user_input = input()

    try:
        user_input = int(user_input)
    except ValueError:
        print('Incorrect input')
        continue

    if user_input == 1:
        for item in fibo(number):
            print(item, end=' ')
        print()
    elif user_input == 2:
        break
    else:
        print('Incorrect input')
