'''
Created on Oct 2, 2018

@author: leonardo
'''

# Import Qiskit Terra
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, IBMQ
from qiskit.tools.monitor import job_monitor
from Qconfig import APItoken
from utils import print_job_execution_information
from numpy import pi



"""
Set your API Token.
You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
looking for "Personal Access Token" section.
"""
QX_TOKEN = APItoken



"""
Authenticate with the IBM Q API in order to use online devices.
You need the API Token.
The account information is need to be stored locally on disk only once.
To store account information locally on disk, uncomment the next line.
"""
# print("Storing account information locally on disk ...")
# IBMQ.save_account(QX_TOKEN)

# The next line is mandatory to load the account infos stored
print("\nLoading account ...")
IBMQ.load_accounts()
# print_dict(IBMQ.stored_accounts()[0])



"""
########### CREATING THE CIRCUIT ##########
"""

print("\nCreating the circuit ...")

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



"""
Selecting backend of available devices.
"""
print("\nGetting backend ...")
backend_ibmq = IBMQ.get_backend('ibmqx4')



"""
####### Compile and run the Quantum circuit on a device backend #########
""" 
print("\nExecuting ...")
job_ibmq = execute(qc, backend=backend_ibmq, shots=8*1024)

# print("\nGo to job monitor")
# job_monitor(job_ibmq)
# print("\nLeft of the job monitor")

  
"""
Getting execution information
"""
print_job_execution_information(job_ibmq)

