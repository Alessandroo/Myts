def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance()


@singleton
class MyClass(object):
    def __init__(self):
        self.values = []


def main():
    x = MyClass
    x.values.append(123)

    y = MyClass
    print(y.values)

    MyClass.values.append(100)
    print(MyClass.values)


if __name__ == "__main__":
    main()