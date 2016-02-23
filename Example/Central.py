import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--task', type=int)
args = parser.parse_args()

if args.task == 1:
    import Task.task1
elif args.task == 2:
    import Task.task2
else:
    print('Number should be 1..2')