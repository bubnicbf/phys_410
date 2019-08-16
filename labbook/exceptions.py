#!/usr/bin/python2
# -*- coding: utf-8 -*-

class LabBookAlreadyExistsError(Exception):
    pass

class LabBookNotFoundError(Exception):
    pass

class UUIDNotFoundError(Exception):
    pass

class AmbiguousUUIDError(Exception):
    pass
