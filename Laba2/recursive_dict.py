class RecDict(dict):
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        else:
            self[key] = RecDict()
            return self[key]


def main():
    a = RecDict({12: {13: {14: '45'}}})
    a[24][18] = '87'
    a[24][15] = '96'
    print(a[12][13][14])
    print(a)


if __name__ == '__main__':
    main()
