# -*- coding: utf-8 -*-

from qiskit import Aer, execute
import Aer_Simulator_Type as AerSimType

def get_backend(simulator_type):
    if simulator_type == AerSimType.Type.StateVector:
        return Aer.get_backend('statevector_simulator')

    elif simulator_type == AerSimType.Type.Unitary:
        return Aer.get_backend('unitary_simulator')

    elif simulator_type == AerSimType.Type.Qasm:
        return Aer.get_backend('qasm_simulator')

    elif simulator_type == AerSimType.Type.Pulse:
        return Aer.get_backend('pulse_simulator')

    else:
        raise ValueError("Found unknown Aer simulator: {0}".format(simulator_type))
