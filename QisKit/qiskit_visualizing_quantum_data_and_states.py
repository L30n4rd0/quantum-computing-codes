'''
Created on Oct 27, 2018

@author: leonardo
'''

# useful additional packages 
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
from pprint import pprint
from scipy import linalg as la

# import state tomography functions
from qiskit.tools.visualization import plot_histogram, plot_state

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import Aer

from utils import printDict, ghz_state, superposition_state

"""
Build the quantum circuit. We are going to build two circuits a GHZ over 3 qubits 
and a superpositon over all 3 qubits
""" 

n = 2  # number of qubits 
q = QuantumRegister(n)
c = ClassicalRegister(n)

# quantum circuit to make a GHZ state 
ghz = ghz_state(q, c, n)
ghz.measure(q, c)

# quantum circuit to make a superposition state 
superposition = superposition_state(q, c)
superposition.measure(q, c)

# measure_circuit = QuantumCircuit(q,c)
# measure_circuit.measure(q, c)

# execute the quantum circuit 
backend = Aer.get_backend('qasm_simulator') # the device to run on
circuits = [ghz, superposition]
job = execute(circuits, backend, shots=1000)

print(job.result().get_counts(circuits[0]))
print(job.result().get_counts(circuits[1]))

# print(job.result().get_data())
# job_dict = job.result().get_data()
# printDict(job_dict)

plot_histogram(job.result().get_counts(circuits[0]))
plot_histogram(job.result().get_counts(circuits[1]),options={'number_to_keep': 15})
