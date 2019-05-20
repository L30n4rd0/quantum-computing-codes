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

q = QuantumRegister(1)
# q[4]
# q[3]
# q[2]
# q[1]
# q[0]

qc = QuantumCircuit(q)

# Decomposition of next matrix
# [[1, 0, 0, 0],
#  [0,-1, 0, 0],
#  [0, 0, 1, 0],
#  [0, 0, 0, 1]]

# {'name': 'u3', 'args': [0], 'params': (3.141592653589793, 0.0, -3.141592653589793)}
# {'name': 'u3', 'args': [1], 'params': (3.141592653589793, 0.0, -4.71238898038469)}
# {'name': 'cx', 'args': [1, 0], 'params': ()}
# {'name': 'u1', 'args': [0], 'params': (0.0, 0.0, 3.141592653589793)}
# {'name': 'u2', 'args': [1], 'params': (1.5707963267948966, 3.141592653589793, -3.141592653589793)}
# {'name': 'cx', 'args': [0, 1], 'params': ()}
# {'name': 'u2', 'args': [1], 'params': (1.5707963267948966, 0.0, 0.0)}
# {'name': 'cx', 'args': [1, 0], 'params': ()}
# {'name': 'u3', 'args': [0], 'params': (3.141592653589793, 0.0, -4.440892098500626e-16)}
# {'name': 'u3', 'args': [1], 'params': (3.141592653589793, 0.0, -1.5707963267948966)}

# qc.u3(3.141592653589793, 0.0, -3.141592653589793, q[1])
# qc.u3(3.141592653589793, 0.0, -4.71238898038469, q[0])
# qc.cx(q[0], q[1])
# qc.u3(0.0, 0.0, 3.141592653589793, q[1])
# qc.u3(1.5707963267948966, 3.141592653589793, -3.141592653589793, q[0])
# qc.cx(q[1], q[0])
# qc.u3(1.5707963267948966, 0.0, 0.0, q[0])
# qc.cx(q[0], q[1])
# qc.u3(3.141592653589793, 0.0, -4.440892098500626e-16, q[1])
# qc.u3(3.141592653589793, 0.0, -1.5707963267948966, q[0])





# qc.u3(0.0, 0.0, 0.0, q[0])
# qc.u3(0.0, 0.0, -1.5707963267948966, q[1])
# qc.cx(q[1], q[0])
# qc.u3(0.0, 0.0, 1.5707963267948966, q[0])
# qc.u3(1.5707963267948966, 3.141592653589793, -3.141592653589793, q[1])
# qc.cx(q[0], q[1])
# qc.u3(1.5707963267948966, 0.0, 0.0, q[1])
# qc.cx(q[1], q[0])
# qc.u3(0.0, 0.0, -1.5707963267948968, q[0])
# qc.u3(0.0, 0.0, 3.1415926535897936, q[1])





### c_not
# qc.u2([0], 'params': (1.5707963267948966, 1.5707963267948966, -1.5707963267948966)}
# qc.u2([1], 'params': (1.5707963267948966, -4.71238898038469, 1.5707963267948966)}
# qc.cx([1, 0], 'params': ()}
# qc.u1([0], 'params': (0.0, 0.0, 1.5707963267948966)}
# qc.u3([1], 'params': (-1.5707963267948968, 0.0, 0.0)}
# qc.cx([0, 1], 'params': ()}
# qc.u3([1], 'params': (3.141592653589793, 0.0, 0.0)}
# qc.cx([1, 0], 'params': ()}
# qc.u2([0], 'params': (1.5707963267948966, 0.0, -3.1415926535897936)}
# qc.u1([1], 'params': (0.0, 0.0, 1.5707963267948966)}


### c_not
# qc.u3(1.5707963267948966, 1.5707963267948966, -1.5707963267948966, q[1])
# qc.u3(1.5707963267948966, -4.71238898038469, 1.5707963267948966, q[0])
# qc.cx(q[0], q[1])
# qc.u3(0.0, 0.0, 1.5707963267948966, q[1])
# qc.u3(-1.5707963267948968, 0.0, 0.0, q[0])
# qc.cx(q[1], q[0])
# qc.u3(3.141592653589793, 0.0, 0.0, q[0])
# qc.cx(q[0], q[1])
# qc.u3(1.5707963267948966, 0.0, -3.1415926535897936, q[1])
# qc.u3(0.0, 0.0, 1.5707963267948966, q[0])


qc.u3(0.9272952180016123, 2.220446049250313e-16, 3.141592653589793, q[0])

# qc.u3(1.2309594197353562, 2.220446049250313e-16, 3.141592653589793, q[0])


# c_3_x
# qc.ccx(q[3], q[2], q[1])
# qc.x(q[1])
# qc.cx(q[1], q[0])
# qc.x(q[1])
# qc.ccx(q[3], q[2], q[1])

# cz
# qc.cz(q[1], q[0])

# ccz
# qc.h(q[0])
# qc.ccx(q[2], q[1], q[0])
# qc.h(q[0])

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
# qc.cx(q[1], q[0])
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
print("Complex")
for row in final_matrix:
    print(row)

print("Real")
for row in final_matrix:
    print(row.real)

