'''
Created on Oct 2, 2018

@author: leonardo
'''

# Import Qiskit Terra
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, compile, IBMQ, Aer
from qiskit.tools.monitor import job_monitor
from Qconfig import APItoken
from utils import print_dict, print_list, list_executed_jobs_on_backend,\
    list_backend_information_status, cancel_all_jobs_on_backend,\
    print_job_execution_information
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
# print_dict(IBMQ.stored_accounts()[0])

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
      
# Add a H gate on qubit 0, putting this qubit in superposition.
qc.h(q[0])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
qc.cx(q[0], q[1])
# Add a Measure gate to see the state.
qc.measure(q, c)



""" 
See a list of available devices.
"""
# print("\nIBMQ backends: ")
# print_list(IBMQ.backends())

# List of available devices beckend
# ibmqx4
# ibmq_16_melbourne
# ibmq_qasm_simulator

"""
Selecting backend of available devices.
"""
print("\nGetting backend ...")
backend_ibmq = IBMQ.get_backend('ibmqx4')

"""
Getting information of the selected backend
"""
# list_backend_information_status(backend_ibmq)


"""
####### Compile and run the Quantum circuit on a device backend #########
""" 


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
# print("\nExecuting ...")
# job_ibmq = execute(qc, backend=backend_ibmq, shots=1024)
# 
# print("\nGo to job monitor")
# job_monitor(job_ibmq)
# print("\nLeft of the job monitor")


"""
Getting executed jobs on backend
"""
# list_executed_jobs_on_backend(backend_ibmq)


"""
Canceling all jobs on backend
"""
# cancel_all_jobs_on_backend(backend_ibmq)


"""
Canceling job by id
"""
# backend_ibmq.retrieve_job('5bd3a2154df859003d31ad0c').cancel()


"""
Retrieving job by id
"""
job_ibmq = backend_ibmq.retrieve_job('5cb4ab74a5d9170065d419d8')

 
"""
Getting execution information
"""
print_job_execution_information(job_ibmq)

   
"""
Getting results
"""
result_ibmq = job_ibmq.result()
        
# Show the results.
print("\nRESULTS")
print(result_ibmq)
    
print("\nresult_counts")
print(result_ibmq.get_counts())
# print_dict(result_ibmq)

