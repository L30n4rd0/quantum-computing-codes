'''
Created on Feb 11, 2019

@author: leonardo
'''

# Import the Qiskit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.tools.visualization import plot_histogram
from utils import print_dict, print_job_execution_information
from numpy import pi



# Numbers of qubits that will be used in the circuit
numbers_of_qubits = 4

# Create a Quantum Register with n qubits.
q = QuantumRegister(numbers_of_qubits)

# Create a Classical Register with n bits.
c = ClassicalRegister(numbers_of_qubits)

# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Add a H gate on qubit 0, putting this qubit in superposition (divider).
qc.h(q)

# Applying oracle on the down slit (auxiliary qubit equals to 1)
# 2 qubits
# qc.cz(q[1], q[0])

# 3 qubits
# qc.h(q[0])
# qc.ccx(q[2], q[1], q[0])
# qc.h(q[0])

# 4 qubits
qc.cu1(pi/4, q[3], q[0])
qc.cx(q[3], q[2])
qc.cu1(-pi/4, q[2], q[0])
qc.cx(q[3], q[2])
qc.cu1(pi/4, q[2], q[0])
qc.cx(q[2], q[1])
qc.cu1(-pi/4, q[1], q[0])
qc.cx(q[3], q[1])
qc.cu1(pi/4, q[1], q[0])
qc.cx(q[2], q[1])
qc.cu1(-pi/4, q[1], q[0])
qc.cx(q[3], q[1])
qc.cu1(pi/4, q[1], q[0])


# Applying controlled_u_1
qc.z(q[0])

# Add a H gate on qubit 0, putting this qubit in superposition (combiner).
qc.h(q[0])

# Add a Measure gate to see the state.
qc.measure(q, c)



# See a list of available local simulators
# print("Aer backends: ", Aer.backends())

# Compile and run the Quantum circuit on a simulator backend
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim)


"""
Getting execution information
"""
print_job_execution_information(job_sim)



# # Show the results
# result_sim = job_sim.result()
# print("Simulation status: ", result_sim.status)
# # print(result_sim.get_counts(qc))
# print("get_counts")
# print_dict(result_sim.get_counts())


# plot_histogram(result_sim.get_counts(), title='Histogram')

