# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)

# Applies the Hadamard gate to 1st bit
qc.h(0)

# Applies the CNOT gate to 1st bit
# 0: control Q-bit
# 1: target Q-bit
qc.cx(0, 1)

# Draws the circuit
qc.draw(output='mpl')

plt.show()