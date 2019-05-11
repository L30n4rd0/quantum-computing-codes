'''
Created on Sep 27, 2018

@author: leonardo
'''

# Import the Qiskit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.tools.visualization import plot_histogram, plot_state_city
from utils import print_dict

# Numbers of qubits that will be used in the circuit
numbers_of_qubits = 2

# Create a Quantum Register with n qubits.
q = QuantumRegister(numbers_of_qubits)
# Create a Classical Register with n bits.
c = ClassicalRegister(numbers_of_qubits)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)


# Add a H gate on qubit 1, putting this qubit in superposition.
qc.h(q[1])
  
# Add a CX (CNOT) gate on control qubit 1 and target qubit 0, putting
# the qubits in a Bell state.
qc.cx(q[1], q[0])

 
# Add a Measure gate to see the state.
qc.measure(q, c)

# See a list of available local simulators
# print("Aer backends: ", Aer.backends())

# Compile and run the Quantum circuit on a simulator backend
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend_sim)
result_sim = job_sim.result()

# Show the results
print("Simulation status: ", result_sim.status)
# print(result_sim.get_counts(qc))
print("get_counts")
print_dict(result_sim.get_counts())

# plot_histogram(result_sim.get_counts(), title='Bell-State counts')

