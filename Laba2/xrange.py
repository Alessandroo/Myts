class Xrange:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("xrange() arg 3 must not be zero")
        if not stop:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __getitem__(self, item):
        return self.start + (item - 1) * self.step

    def __iter__(self):
        return self

    def __str__(self):
        return 'xrange({0}, {1}, {2})'.format(self.start, self.stop, self.step)

    def __len__(self):
        if self.start > self.stop and self.step > 0:
            return 0
        if self.start < self.stop and self.step < 0:
            return 0
        return int((self.stop - self.start - 1) / self.step) + 1

    def __next__(self):
        if self.step > 0:
            if self.current < self.stop:
                result = self.current
                self.current += self.step
                return result
            else:
                self.current = self.start
                raise StopIteration
        else:
            if self.current > self.stop:
                result = self.current
                self.current += self.step
                return result
            else:
                self.current = self.start
                raise StopIteration


def main():
    a = Xrange(10)
    print(a)
    print("Length: {0}".format(len(a)))

    for i in a:
        print(i)
    print("\n")

    a = Xrange(10, 5)
    print(a)
    print("Length: {0}".format(len(a)))

    for i in a:
        print(i)
    print("\n")

    a = Xrange(21, -3, -2)
    print(a)
    print("Length: {0}".format(len(a)))

    for i in a:
        print(i)
    print("\n")


if __name__ == '__main__':
    main()
