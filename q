#!/usr/bin/env python


import argparse
from quickly import quickly


def main(args):
    quickly.Quickly()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do a quick cd without typing the whole path')

    parser.add_argument('add', help="To remember this directory", nargs=1, required=False)
    parser.add_argument('as', help="And reference that directory with this key", nargs=1, required=False)
    parser.add_argument('rm', help="Remove a key", nargs=1, required=False)
    args = parser.parse_args()

    main(args)
