#!/usr/bin/python
# -*- coding: utf-8 -*-

from blitzdb import Document, FileBackend

DoesNotExist = Document.DoesNotExist

__all__ = ['Experiment, FileBackend', 'DoesNotExist']

class Experiment(Document):
    pass
