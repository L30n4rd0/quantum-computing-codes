'''
Created on Oct 2, 2018

@author: leonardo
'''

# Import Qiskit Terra
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, IBMQ
from qiskit.tools.monitor import job_monitor
from Qconfig import APItoken
from utils import print_dict, print_job_execution_information



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
numbers_of_qubits = 5

# Create a Quantum Register with n qubits.
q = QuantumRegister(numbers_of_qubits)

# Create a Classical Register with n bits.
c = ClassicalRegister(numbers_of_qubits)

# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Add a H gate on qubit 2 and 1, putting qubits work in superposition
qc.h(q[4])
qc.h(q[3])
qc.h(q[2])
qc.h(q[1])

# Add divider gate on qubit 0

# qwd gate to n_qbits=3, m_marked_itens=1
# qc.u3(1.2309594173407747, 2.220446049250313e-16, 3.141592653589793, q[0])

# qwd gate to n_qbits=4, m_marked_itens=3
qc.u3(0.9272952180016123, 2.220446049250313e-16, 3.141592653589793, q[0])

# Applying oracle

# 3 qubits
qc.h(q[0])
qc.ccx(q[2], q[1], q[0])
qc.h(q[0])

# Applying controlled_u_1
qc.z(q[0])

# Add combiner gate on qubit 0

# qwc gate to n_qbits=3, m_marked_itens=1
# qc.u3(1.2309594173407747, 2.220446049250313e-16, 3.141592653589793, q[0])

# qwc gate to n_qbits=4, m_marked_itens=3
qc.u3(0.9272952180016123, 2.220446049250313e-16, 3.141592653589793, q[0])

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
job_ibmq = execute(qc, backend=backend_ibmq, shots=1024)

# print("\nGo to job monitor")
# job_monitor(job_ibmq)
# print("\nLeft of the job monitor")

  
"""
Getting execution information
"""
print_job_execution_information(job_ibmq)

