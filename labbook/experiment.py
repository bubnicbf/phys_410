#!/usr/bin/python2
# -*- coding: utf-8 -*-

__all__ = ['ExperimentRunner']

import sys
import os
import time
import select
from subprocess import Popen, PIPE

class ExperimentRunner(object):
    def __init__(self, path, uuid, command_line):
        self.path = path
        self.uuid = uuid
        self.command_line = command_line
        self.start_time = None
        self.run_time = None

    def run(self):
        log = open(os.path.join(self.path, 'output.log'), 'w')

        self.start_time = time.time()
        try:
            proc = Popen(self.command_line.split(), stdout=PIPE, stderr=PIPE)
            while proc.poll() is None:
                rlist, wlist, xlist = select.select([proc.stdout, proc.stderr], [], [])
                for fd in rlist:
                    if fd == proc.stdout:
                        data = fd.read()
                        sys.stdout.write(data)
                        log.write(data)
                    if fd == proc.stderr:
                        data = fd.read()
                        sys.stderr.write(data)
                        log.write(data)
        except Exception as exc:
            raise exc
        finally:
            self.run_time = time.time() - self.start_time

    def collect(self):
        for path in os.listdir('.'):
            path = os.path.join(os.path.abspath('.'), path)
            mtime = os.path.getmtime(path)
            if mtime > self.start_time:
                yield path
