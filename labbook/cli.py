#!/usr/bin/python2
# -*- coding: utf-8 -*-

__all__ = ['Interface', 'main']

import os
import datetime

from .exceptions import *
from .labbook import LabBook

class Interface(object):
    def __init__(self):
        pass

    def create(self, args):
        path = os.path.abspath(args.path)
        try:
            labbook = LabBook.create(path)
        except LabBookAlreadyExistsError as exc:
            print exc.message
        else:
            print("I created a labbook for you in '{0}'. Get to work!".format(labbook.path))

    def run(self, args):
        path = os.getcwd()
        try:
            labbook = LabBook(path)
        except LabBookNotFoundError as exc:
            print(exc.message)
        else:
            labbook.run(args.command_line)

    def log(self, args):
        path = os.getcwd()
        try:
            labbook = LabBook(path)
        except LabBookNotFoundError as exc:
            print(exc.message)
        else:
            for experiment in labbook.log():
                print "{date}: {cmd} ({uuid})".format(
                        date = datetime.datetime.fromtimestamp(float(experiment[3])).strftime('%a %b %d %H:%M:%S %Y'),
                        cmd = experiment[1],
                        uuid = experiment[0]
                        )
                if experiment[5]:
                    print("\n    {0}\n".format(experiment[5]))
                else:
                    print("\n    (no comment)\n")


def main():
    import argparse

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command')

    run_parser = sub.add_parser('run')
    run_parser.add_argument('command_line', type=str, nargs='+')

    log_parser = sub.add_parser('log')
    
    log_parser = sub.add_parser('create')
    log_parser.add_argument('path', type=str)

    args = parser.parse_args()
    
    interface = Interface()
    getattr(interface, args.command)(args)
