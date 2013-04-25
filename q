#!/usr/bin/env python


import argparse
from quickly import quickly


def main(args):
    quickly.Quickly()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do a quick cd without typing the whole path')

    parser.add_argument('-a', '--add', help='Add a new key for a given path', nargs=2, metavar=('KEY', 'PATH'))

    parser.add_argument('-e', '--edit', help='Edit a key with a new path', nargs=2, metavar=('KEY', 'PATH'))

    parser.add_argument('-rm', '--remove', help='Remove a key', metavar='KEY')

    parser.add_argument('-ls', '--list', help='List all keys')

    args = parser.parse_args()

    main(args)
