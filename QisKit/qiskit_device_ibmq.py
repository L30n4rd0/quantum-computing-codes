'''
Created on Oct 2, 2018

@author: leonardo
'''

# Import Qiskit Terra
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, compile, IBMQ, Aer
from qiskit.tools.monitor import job_monitor
from Qconfig import APItoken
from utils import printDict, printList
import time

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
# printDict(IBMQ.stored_accounts()[0])

"""
########### CREATING THE CIRCUIT ##########
"""

print("\nCreating the circuit ...")

# Numbers of registers that will be used in the circuit
numbers_of_registers = 2

# Create a Quantum Register with 2 qubits.
q = QuantumRegister(numbers_of_registers)
# Create a Classical Register with 2 bits.
c = ClassicalRegister(numbers_of_registers)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Add a H gate on qubit 0, putting this qubit in superposition (divider).
qc.h(q)

# Applying oracle
qc.cz(q[1], q[0])

# Applying controlled_u_1
qc.z(q[0])

# Add a H gate on qubit 0, putting this qubit in superposition (combiner).
qc.h(q[0])

# Add a Measure gate to see the state.
qc.measure(q, c)



# # Create a Quantum Register with 2 qubits.
# q = QuantumRegister(2)
#    
# # Create a Classical Register with 2 bits.
# c = ClassicalRegister(2)
#    
# # Create a Quantum Circuit
# qc = QuantumCircuit(q, c)
#      
# # Add a H gate on qubit 0, putting this qubit in superposition.
# qc.h(q[0])
# # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# # the qubits in a Bell state.
# qc.cx(q[0], q[1])
# # Add a Measure gate to see the state.
# qc.measure(q, c)



""" 
See a list of available devices.
"""
# print("\nIBMQ backends: ")
# printList(IBMQ.backends())

# List of available devices beckend
# ibmqx4
# ibmq_16_melbourne
# ibmq_qasm_simulator

"""
Selecting backend of available devices.
"""
print("\nGetting backend ...")
backend_ibmq = IBMQ.get_backend('ibmq_16_melbourne')

"""
Getting information of the selected backend
"""
# print("provider: " , backend_ibmq.provider)
# print("name: " , backend_ibmq.name())
# print("status: " , backend_ibmq.status())
# print("configuration: " , backend_ibmq.configuration())
# print("properties: " , backend_ibmq.properties())

"""
####### Compile and run the Quantum circuit on a device backend #########
""" 

"""
Getting executed jobs on backend
"""
# print("\nGetting executed jobs infos ...")
# jobs = backend_ibmq.jobs()
#      
# for job in jobs:
#     print(str(job.job_id()) + " " + 
#           str(job.status()) + " " + 
#           str(job.creation_date()) + " " +
#           str(job.queue_position())
#           )


#     if job.status().name != 'DONE':
#         print("Canceling the job ...")
#         job.cancel()

"""
Canceling job by id
"""
# backend_ibmq.retrieve_job('5bd3a2154df859003d31ad0c').cancel()

"""
Retrieving job by id
"""
# job_ibmq = backend_ibmq.retrieve_job('5c63636e5a747200565b2c42')

# Job id: 5c63636e5a747200565b2c42
# State: 2280 seconds
# Status: QUEUED
# Queue position: 817

"""
Compile and run
"""
# # Compile
# print("\nCompiling ...")
# quantum_object = compile(circuits=qc, backend=backend_ibmq)
#  
# # Rum (asynchronous running of jobs)
# print("\nRunning ...")
# job_ibmq = backend_ibmq.run(quantum_object)

"""
Alternative form to compile and run (execute)
"""
print("\nExecuting ...")
job_ibmq = execute(qc, backend=backend_ibmq, shots=1024)

# print("Go to job monitor")
# job_monitor(job_ibmq)
# print("Left of the job monitor")
 
"""
Getting execution information
"""
lapse = 0
interval = 60
while job_ibmq.status().name != 'DONE':
    print("\n")
    print("Job id: " + job_ibmq.job_id())
    print("State: " + str(interval * lapse) + " seconds")
    print("Status: " + job_ibmq.status().name)
    print("Queue position: " + str( job_ibmq.queue_position() ))
    print(".......................................")
     
    if (job_ibmq.queue_position() == 0):
        break
         
    time.sleep(interval)
    lapse += 1
         
print("\nExecution final status: " + job_ibmq.status().name)
   
"""
Getting results
"""
result_ibmq = job_ibmq.result()
       
# Show the results.
print("\nRESULTS")
print(result_ibmq)
   
print("\nresult_counts")
print(result_ibmq.get_counts())
# printDict(result_ibmq)
