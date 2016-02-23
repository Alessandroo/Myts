from modules.interactive import writen

print('Task 1.3')

while True:
    print('1. Code!')
    print('2. Exit')
    user_input = input()

    try:
        user_input = int(user_input)
    except ValueError:
        print('Incorrect input')
        continue

    if user_input == 1:
        writen()
    elif user_input == 2:
        break
    else:
        print('Incorrect input')
