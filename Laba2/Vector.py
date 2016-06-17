from itertools import starmap, zip_longest
from operator import add, mul, sub


class Vector:
    def __init__(self, arg, dimension_error=True):
        self.dimension_error = dimension_error
        if isinstance(arg, int):
            if arg < 1:
                raise ValueError('Count of Vector arguments should be more 0')
            self.vector = [0] * arg
        elif isinstance(arg, list):
            self.vector = arg
        else:
            raise TypeError('arg Vector() should be int or list')

    @property
    def length(self):
        return sum([n * n for n in self]) ** 0.5

    @property
    def dimension(self):
        return len(self.vector)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('In operation with Vector use only other Vector')
        if self.dimension_error:
            if self.dimension == other.dimension:
                return Vector(list(map(lambda x, y: x + y, self, other)))
            else:
                raise ValueError('Dimensions of Vectors are differ')
        return Vector(list(starmap(add, zip_longest(self, other, fillvalue=0))))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('In operation with Vector use only other Vector')
        if self.dimension_error:
            if self.dimension == other.dimension:
                return Vector(list(map(lambda x, y: x - y, self, other)))
            else:
                raise ValueError('Dimensions of Vectors are differ')
        return Vector(list(starmap(sub, zip_longest(self.vector, other, fillvalue=0))))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([num * other for num in self.vector])
        elif isinstance(other, Vector):
            if self.dimension_error:
                if self.dimension == other.dimension:
                    return sum(map(lambda x, y: x * y, self, other))
                else:
                    raise ValueError('Dimensions of Vectors are differ')
            return sum(starmap(mul, zip_longest(self.vector, other, fillvalue=0)))
        else:
            raise TypeError('In operation with Vector use only other Vector')

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.vector == other.vector

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0 or key > len(self.vector) - 1:
                raise IndexError('Index out of range')
            return self.vector[key]
        if isinstance(key, slice):
            return self.vector.__getitem__(key)
        else:
            raise TypeError('Index should be int or slice')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if key < 0 or key > len(self.vector) - 1:
                raise IndexError('Index out of range')
            self.vector[key] = value
        else:
            raise TypeError('Index should be int')

    def __str__(self):
        return str(self.vector)


def main():
    a = Vector([1, 7, 8, 9])
    b = Vector([1, 7, 8, 9])
    print(a)
    print(a.length)
    print(b)
    print(b.length)
    print(a == b)
    print(a[1])
    print(a + b)
    print(a * b)
    print(a - b)


if __name__ == '__main__':
    main()
