'''
Created on Feb 6, 2019

@author: leonardo
'''
# Useful additional packages
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from math import pi

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import circuit_drawer
from qiskit.quantum_info import state_fidelity
from qiskit import Aer

# print("Backends list")
# print(Aer.backends())

backend = Aer.get_backend('unitary_simulator')

q = QuantumRegister(3)
# q[4]
# q[3]
# q[2]
# q[1]
# q[0]

qc = QuantumCircuit(q)

# c_3_x
# qc.ccx(q[3], q[2], q[1])
# qc.x(q[1])
# qc.cx(q[1], q[0])
# qc.x(q[1])
# qc.ccx(q[3], q[2], q[1])


# ccz
qc.h(q[0])
qc.ccx(q[2], q[1], q[0])
qc.h(q[0])

# c_3_z
# qc.h(q[0])
# qc.ccx(q[3], q[2], q[1])
# qc.x(q[1])
# qc.cx(q[1], q[0])
# qc.x(q[1])
# qc.ccx(q[3], q[2], q[1])
# qc.h(q[0])

# c_4_z
# qc.ccx(q[4], q[3], q[0])
# qc.h(q[1])
# qc.ccx(q[2], q[0], q[1])
# qc.h(q[1])
# qc.ccx(q[4], q[3], q[0])

# qc.h(q[1])
# qc.h(q[0])
# qc.cx(q[2], q[0])
# qc.cz(q[2], q[1])
# qc.cz(q[1], q[0])


# qc.iden(q)

# qc.z(q[1])
# qc.y(q)

# qc.cz(q[1], q[0])
# qc.cz(q[2], q[1])


# qc.cz(q[2], q[0])
# qc.z(q[2])
# qc.z(q[1])
# qc.z(q[1])
# qc.z(q)

# qc.h(q)
# qc.h(q)

# qc.u0(pi/2,q)
# qc.u0(pi/2,q)

# qc.u1(pi/2,q)
# qc.u1(pi/2,q)

# qc.u2(pi/2,pi/2,q)
# qc.u2(pi/2,pi/2,q)

# qc.u3(pi/2,pi/2,pi/2,q)
# qc.u3(0, 0, pi, q)

# qc.h(q)
# qc.cx(q[0], q[1])

# qc.draw()

# # Add a H gate on qubit 0, putting this qubit in superposition (divider).
# qc.h(q)
# 
# # Applying controlled_u_1
# qc.z(q[0])
# 
# # Add a H gate on qubit 0, putting this qubit in superposition (combiner).
# qc.h(q[0])

job = execute(qc, backend)
final_matrix = job.result().get_unitary(qc, decimals=3)
final_matrix = np.array(final_matrix, dtype = int)

for i in range(len(final_matrix)):
    print(final_matrix[i])


