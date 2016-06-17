import argparse
import random
import string


def init_parser():
    parser = argparse.ArgumentParser('File maker')

    parser.add_argument('name_file')
    parser.add_argument('--fixed', nargs='?', type=int, const=5, default=False)
    parser.add_argument('-n', '--numeric', action='store_true')
    parser.add_argument('-t', '--field-separator', default='\t')
    parser.add_argument('--line-separator', default='\n')
    parser.add_argument('--count-string', type=int, default=10000)
    return parser


def generation_file(rule):
    with open(rule.name_file, mode='w') as file:
        if rule.numeric:
            numeric = string.digits
        else:
            numeric = string.ascii_letters + string.digits

        for line in range(rule.count_string):
            if not rule.fixed:
                fixed = random.randint(4, 10)
            else:
                fixed = rule.fixed
            for word in range(fixed):
                file.write(
                    ''.join(random.choice(numeric) for x in range(random.randint(10, 20))))
                file.write(rule.field_separator)
            file.write(rule.line_separator)


def main():
    parser = init_parser()
    rule = parser.parse_args()
    if rule:
        generation_file(rule)


if __name__ == '__main__':
    main()