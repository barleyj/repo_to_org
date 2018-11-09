#!/usr/bin/env python

import os

import click

ignore = {'.git', '.bundle', 'venv', 'files', 'spec'}

@click.command()
@click.argument('dir')
def to_org(dir):
    for root, dirnames, filenames in os.walk(dir):
        found_dirs = ignore & set(root.split('/'))
        if found_dirs:
            continue
        indent = root.count('/')
        print "{} {}".format('*' * indent, os.path.basename(root))
#        print dirnames
        for f in filenames:
            print "{} {}".format('*' * (indent + 1), os.path.splitext(f)[0])

if __name__ == '__main__':
    to_org()
