'''
Created on Oct 1, 2018

@author: leonardo
'''

from qiskit import QuantumCircuit
import numpy as np
import time

def print_dict(dictionary):
    
    try:
        for item in dictionary.items():
            try:
                item[1].items()
                print('<<' , item[0] , '>>')
                
                print_dict(item[1])
                
                print('<<' , item[0] , '>>')
            
            except:
                print(item[0] , ':' , item[1])
                pass
            
    except:
        pass
    


def print_list(anyList):
    for item in anyList:
        print(item)
        



def print_job_execution_information(job):
    lapse = 0
    interval = 60
    
    while True:
        print("\n")
        print("Job id: " + job.job_id())
        print("State: " + str(interval * lapse) + " seconds")
        print("Status: " + job.status().name)
        print("Queue position: " + str( job.queue_position() ))
        print(".......................................")
           
#         if (job.queue_position() == 0):
#             break
               
        time.sleep(interval)
        lapse += 1
        
        if job.status().name == 'DONE':
            break
               
    print("\nExecution final status: " + job.status().name)
    
    """
    Getting results
    """
    result_ibmq = job.result()
        
    # Show the results.
    print("\nRESULTS")
    print(result_ibmq)
              
    print("\nResult_counts")
    print(result_ibmq.get_counts())
      
    print("\n")
    print_dict(result_ibmq.get_counts())



def list_executed_jobs_on_backend(backend):
    jobs = backend.jobs()
         
    for job in jobs:
        print(
            str(job.job_id()) + " " + 
            str(job.status()) + " " + 
            str(job.creation_date()) + " " +
            str(job.queue_position())
        )
        


def cancel_all_jobs_on_backend(backend):
    jobs = backend.jobs()
         
    for job in jobs:
        if job.status().name != 'DONE':
            print("Canceling the job ...")
            job.cancel()
        


def list_backend_information_status(backend):
    print("provider: " , backend.provider)
    print("name: " , backend.name())
    print("status: " , backend.status())
    print("configuration: " , backend.configuration())
    print("properties: " , backend.properties())




def ghz_state(q, c, n):
    # Create a GHZ state
    qc = QuantumCircuit(q, c)
    qc.h(q[0])
    for i in range(n-1):
        qc.cx(q[i], q[i+1])
    return qc



def superposition_state(q, c):
    # Create a Superposition state
    qc = QuantumCircuit(q, c)
    qc.h(q)
    return qc



def over_lap(state1, state2):
    return round(np.dot(state1.conj(), state2))



def state_2_rho(state):
    return np.outer(state, state.conj())



def expectation_value(state, Operator):
    return round(np.dot(state.conj(), np.dot(Operator, state)).real)

