import argparse
import tempfile


buffers = []


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-ls', help="line separator", type=str, default='\n')
    parser.add_argument('-fs', help="field separator", type=str, default='\t')
    parser.add_argument('-fin', help="input file", type=str, default="input.txt")
    parser.add_argument('-fout', help="output file", type=str, default="output.txt")
    parser.add_argument('-bs', help="buffer size", type=int, default=5000)
    parser.add_argument('-rv', help="reverse", action="store_true")
    parser.add_argument('-ch', help="sort check", action="store_true")
    parser.add_argument('-fc', help="fields count", type=int, default=4)
    parser.add_argument('-fsize', help="field size", type=int, default=5)

    return parser.parse_args()


# checks sorted in alphabetical order
def check_sorted(file):
    with open(file) as f:
        prev = f.readline()
        cur = f.readline()

        while cur != '':
            if prev > cur:
                print(prev)
                print(cur)
                return False

            prev = cur
            cur = f.readline()

        return True


def compare(a, b, reverse=False):
    if reverse:
        return a >= b

    return a <= b


def partition(args):
    file = open(args.fin)

    data = []
    cur_pos = 0
    cur_line = file.readline()
    temp = tempfile.TemporaryFile()

    while cur_line:
        data.append(cur_line)
        cur_line = file.readline()
        cur_pos += 1

        if cur_pos > args.bs:
            data.sort(reverse=args.rv)

            for i in range(len(data)):
                temp.write(bytes(data[i], "UTF-8"))

            data = []
            cur_pos = 0
            temp.seek(0)
            buffers.append(temp)
            temp = tempfile.TemporaryFile()

    file.close()


def merge(first, second, args):
    str_size = (args.fsize + 1) * args.fc

    result = tempfile.TemporaryFile()
    first.seek(0)
    second.seek(0)

    fl = first.read(str_size)
    sl = second.read(str_size)

    while fl or sl:
        if not fl:
            result.write(sl)
            sl = second.read(str_size)

        if not sl:
            result.write(fl)
            fl = first.read(str_size)

        if compare(fl, sl, args.rv):
            result.write(fl)
            fl = first.read(str_size)
        else:
            result.write(sl)
            sl = second.read(str_size)

    return result


def main():
    args = parse_args()

    if args.ch:
        print(args.fout + " is sorted: " + str(check_sorted(args.fout)))
    else:
        partition(args)

        while len(buffers) > 1:
            result = merge(buffers.pop(0), buffers.pop(0), args)
            result.seek(0)
            buffers.append(result)

        buffers[0].seek(0)
        file = open(args.fout, "w")
        file.write(buffers[0].read().decode("UTF-8"))

if __name__ == "__main__":
    main()