'''
Created on Oct 27, 2018

@author: leonardo
'''

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute, Aer
from utils import print_list, over_lap, state_2_rho, expectation_value
from qiskit.tools.visualization import plot_state
import numpy as np

n = 2  # number of qubits 
q = QuantumRegister(n)
c = ClassicalRegister(n)

qc = QuantumCircuit(q, c)
qc.h(q[1])

print("Aer.available_backends")
print_list(Aer.backends())

# execute the quantum circuit 
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
state_superposition = job.result().get_statevector(qc)

print("\nget_statevector")
print_list(state_superposition)

# print("\noverlap")
# print(over_lap(state_superposition, state_superposition))
# 


X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
IZ = np.kron(np.eye(2), Z)
ZI = np.kron(Z, np.eye(2))
IX = np.kron(np.eye(2), X)
XI = np.kron(X, np.eye(2))
 
 
# print("\nexpectation_value")
print("Operator Z on qubit 0 is " + str(expectation_value(state_superposition, IZ)))
print("Operator Z on qubit 1 is " + str(expectation_value(state_superposition, ZI)))
print("Operator X on qubit 0 is " + str(expectation_value(state_superposition, IX)))
print("Operator X on qubit 1 is " + str(expectation_value(state_superposition, XI)))


# rho_superposition=state_2_rho(state_superposition)
# print("\nstate_2_rho")
# print(rho_superposition)


# plot_state(rho_superposition,'city')
# 
# plot_state(rho_superposition,'paulivec')
# 
# plot_state(rho_superposition,'qsphere')
# 
# plot_state(rho_superposition,'bloch')

##############################################################################

# n = 2  # number of qubits 
# q = QuantumRegister(n)
# c = ClassicalRegister(n)
# 
# qc2 = QuantumCircuit(q, c)
# qc2.h(q[1])
# qc2.z(q[1])
# 
# 
# # execute the quantum circuit 
# backend = Aer.get_backend('statevector_simulator')
# job = execute(qc2, backend)
# state_neg_superposition = job.result().get_statevector(qc2)
# rho_neg_superposition=state_2_rho(state_neg_superposition)
# 
# plot_state(rho_neg_superposition, 'qsphere')
# 
# plot_state(0.5*rho_neg_superposition + 0.5* rho_superposition, 'qsphere')

