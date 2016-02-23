import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--task', type=int)
args = parser.parse_args()

if args.task == 1:
    import Task.Zad1
elif args.task == 2:
    import Task.Zad2
elif args.task == 3:
    import Task.Zad3
elif args.task == 4:
    import Task.Zad4
else:
    print('Number should be 1..4')