#!/usr/bin/python2
# -*- coding: utf-8 -*-

__all__ = ['LabBook', 'is_labbook']

import os
import shutil
import random
import csv

from .experiment import Experiment
from .exceptions import *

def is_labbook(path):
    return os.path.exists(os.path.join(path, '.labbook'))


def find_labbook(path):
    path = os.path.abspath(path)
    assert path.startswith('/')

    while path != '':
        if is_labbook(path):
            return path
        path = '/'.join(path.split('/')[:-1])


class LabBook(object):
    def __init__(self, path):
        self.path = path
        if (not path) or (not is_labbook(path)):
            raise LabBookNotFoundError("There is no lab book in '{0}'.".format(path))
   
    @classmethod
    def create(cls, path):
        path = os.path.abspath(path)
        if is_labbook(path):
            raise LabBookAlreadyExistsError("It appears like you already keep a labbook in '{0}'.".format(path))

        os.mkdir(os.path.join(path, '.labbook'))
        os.mkdir(os.path.join(path, '.labbook', 'storage'))
        open(os.path.join(path, '.labbook', 'experiments'), 'a')

        return cls(path)

    def run(self, command_line):
        uuid = '{0:032x}'.format(random.getrandbits(128))
        storage_path = os.path.join(self.path, '.labbook', 'storage', uuid)
        os.mkdir(storage_path)
        
        command_line = ' '.join(command_line)
        experiment = Experiment(storage_path, uuid, command_line)

        try:
            experiment.run()
        except Exception as exc:
            raise exc
        finally:
            log = open(os.path.join(self.path, '.labbook', 'experiments'), 'a')
            log_writer = csv.writer(log)
            log_writer.writerow([uuid, command_line, os.getcwd(), round(experiment.start_time, 3), round(experiment.run_time, 3), ""])

            for path in experiment.collect():
                shutil.copy(path, storage_path)

    def log(self):
        log = open(os.path.join(self.path, '.labbook', 'experiments'))
        log_reader = csv.reader(log)
        for experiment in log_reader:
            yield experiment
