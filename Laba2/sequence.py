from itertools import tee


class Sequence:
    def __init__(self, iterable):
        self.sequence = iterable

    def __iter__(self):
        res, self.sequence = tee(iter(self.sequence))
        return res

    def filter(self, fun):
        return Sequence((item for item in self.sequence if fun(item)))

    def __str__(self):
        return str(self.sequence)


def main():
    a = Sequence([e for e in range(5, 250)])
    print(a)
    part_a = a.filter(lambda x: x < 100)
    print(list(part_a))


if __name__ == '__main__':
    main()
