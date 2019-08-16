#!/usr/bin/python2
# -*- coding: utf-8 -*-

__all__ = ['LabBook', 'is_labbook']

import os
import shutil
import random
import csv

from .experiment import ExperimentRunner
from .exceptions import *
from .storage import Experiment, FileBackend, DoesNotExist

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
        
        self.storage = FileBackend(os.path.join(path, '.labbook', 'experiments.db'))
   
    @classmethod
    def create(cls, path):
        path = os.path.abspath(path)
        if is_labbook(path):
            raise LabBookAlreadyExistsError("It appears like you already keep a labbook in '{0}'.".format(path))

        os.mkdir(os.path.join(path, '.labbook'))
        os.mkdir(os.path.join(path, '.labbook', 'storage'))
        #open(os.path.join(path, '.labbook', 'experiments'), 'a')

        return cls(path)

    def run(self, command_line):
        uuid = '{0:032x}'.format(random.getrandbits(128))
        storage_path = os.path.join(self.path, '.labbook', 'storage', uuid)
        os.mkdir(storage_path)
        
        command_line = ' '.join(command_line)
        experiment = ExperimentRunner(storage_path, uuid, command_line)

        try:
            experiment.run()
        except Exception as exc:
            raise exc
        finally:
            self.storage.save(Experiment({
                'uuid': uuid,
                'command_line': command_line,
                'working_directory': os.getcwd(),
                'date': round(experiment.start_time, 3),
                'runtime': round(experiment.run_time, 3),
                'comment': ""
                }))
            self.storage.commit()

            for path in experiment.collect():
                shutil.copy(path, storage_path)

    def log(self):
        for experiment in self.storage.filter(Experiment, {}):
            yield experiment


    def set_comment(self, uuid, comment):
        try:
            experiment = self.storage.get(Experiment, {'uuid': {'$regex': uuid + '.*'}})
        except Experiment.DoesNotExist:
            raise UUIDNotFoundError("There is no experiment with a (partial) uuid of '{0}'.".format(uuid))
        except Experiment.MultipleObjectsReturned:
            raise AmbiguousUUIDError("There are multiple experiments with a (partial) uuid of '{0}'. Try to be more specific!".format(uuid))
        else:
            experiment.comment = comment
            experiment.save()
            self.storage.commit()
