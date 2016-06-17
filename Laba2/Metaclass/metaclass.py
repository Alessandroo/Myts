class Metaclass(type):
    def __new__(mcs, name, bases, dct):
        file_name = "meta"

        if "file_name" in dct:
            file_name = dct["file_name"]

        with open(file_name) as file:
            for line in file:
                if line != "":
                    attributes = line.strip().split(' ')
                    dct[attributes[0]] = attributes[1]
        return super(Metaclass, mcs).__new__(mcs, name, bases, dct)


class Temp(metaclass=Metaclass):
    pass


def main():
    t = Temp()
    print(t.x)
    print(t.y)
    print(t.z)
    print(t.qwerty)


if __name__ == "__main__":
    main()