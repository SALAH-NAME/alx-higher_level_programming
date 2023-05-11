#!/usr/bin/python3
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    n_args = len(args)

    if n_args == 0:
        print("0 arguments.")
        sys.exit()

    print(f"{n_args} {'argument' if n_args == 1 else 'arguments'}:")
    for index, arg in enumerate(args):
        print(f"{index+1}: {arg}")
