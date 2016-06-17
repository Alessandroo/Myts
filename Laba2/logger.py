import types


class Logger:
    def __init__(self):
        self.logs = []

    def __getattribute__(self, attr):
        if type(object.__getattribute__(self, attr)) is types.MethodType:
            def write_logs(*args, **kwargs):
                result = object.__getattribute__(self, attr)(*args, **kwargs)
                self.logs.append((attr, args, kwargs, result))
                return result

            return write_logs
        else:
            return object.__getattribute__(self, attr)

    def __str__(self):
        result = ''

        for log in self.logs:
            result += 'Method name: {0}, args: {1}, {2}, result: {3}\n'.format(log[0], log[1], log[2], log[3])

        return result


def main():
    class Sum(Logger):
        def s(self, *args):
            result = 0

            for i in args:
                result += i

            return result

    x = Sum()
    print(x.s(1, 2, 3, 4))
    print(x.s(1, 2, 3))
    print(x.s(1, 2))
    print(x)


if __name__ == "__main__":
    main()
