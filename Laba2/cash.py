import random
from freeze import freeze


def cached(f):
    cash = {}

    def cashed_fun(*args, **kwargs):
        element = freeze(args + tuple(kwargs.items()))
        if element in cash:
            print('from cache')
            return cash[element]
        else:
            result = f(*args, **kwargs)
            cash[element] = result
            return result

    return cashed_fun


@cached
def mul(v1, v2):
    return v1 * v2


def main():
    for i in range(20):
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        print(mul(x, y))


if __name__ == '__main__':
    main()
