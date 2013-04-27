#!/usr/bin/env python


import argparse
#import argcomplete
from quickly import quickly


def main(args, q):
    if args.add:
        q.add(args.add[0], args.add[1])
    elif args.edit:
        q.edit(args.edit[0], args.edit[1])
    elif args.remove:
        q.remove(args.remove)
    elif args.list:
        ls = q.list()
        for k, v in ls:
            print('{} -> {}'.format(k, v))
    elif args.key:
        q.cd(args.key)

    q.sync()

if __name__ == '__main__':
    q = quickly.Quickly()

    parser = argparse.ArgumentParser(description='Do a quick cd without typing the whole path')

    parser.add_argument('key', default=1, help="CD to this key")

    parser.add_argument('-a', '--add', metavar=('KEY', 'PATH'), nargs=2, help='Map key to the specified path')
    parser.add_argument('-e', '--edit', metavar=('KEY', 'PATH'), nargs=2, help='Edit the given key with a new path')
    parser.add_argument('-rm', '--remove', metavar='KEY', help='Remove the given key')
    parser.add_argument('-ls', '--list', action='store_true', help='List all keys with mapped paths')

    args = parser.parse_args()
    #argcomplete.autocomplete(parser)

    main(args, q)
