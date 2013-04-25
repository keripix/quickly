#!/usr/bin/env python


import argparse
from quickly import quickly


def main(args):
    q = quickly.Quickly()

    if 'add' in args:
        q.add(args.add[0], args.add[1])
    elif 'edit' in args:
        q.edit(args.edit[0], args.edit[1])
    elif 'remove' in args:
        q.remove(args.remove)
    else:
        print('list')

    q.sync()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do a quick cd without typing the whole path')

    subparsers = parser.add_subparsers()

    parser_add = subparsers.add_parser('add', help='Adding a new key')
    parser_add.add_argument('add', metavar=('KEY', 'PATH'), help='Add a new KEY to the given PATH', nargs=2)

    parser_edit = subparsers.add_parser('edit', help="Edit a key")
    parser_edit.add_argument('edit', metavar=('KEY', 'PATH'), help='Edit a given key with a new path', nargs=2)

    parser_remove = subparsers.add_parser('rm', help="Remove a key")
    parser_remove.add_argument('remove', metavar='KEY', help="Remove the given key")

    args = parser.parse_args()

    main(args)
