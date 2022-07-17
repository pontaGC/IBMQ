# -*- coding: utf-8 -*-

from enum import Enum

class Type(Enum):
    StateVector = 0
    Unitary = 1
    Qasm = 2
    Pulse = 3
