'''
Created on Oct 1, 2018

@author: leonardo
'''

from qiskit import QuantumCircuit
import numpy as np

def printDict(dictionary):
    
    try:
        for item in dictionary.items():
            try:
                item[1].items()
                print('<<' , item[0] , '>>')
                
                printDict(item[1])
                
                print('<<' , item[0] , '>>')
            
            except:
                print(item[0] , ':' , item[1])
                pass
            
    except:
        pass
    
def printList(anyList):
    for item in anyList:
        print(item)
        
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

def overlap(state1, state2):
    return round(np.dot(state1.conj(), state2))

def state_2_rho(state):
    return np.outer(state, state.conj())

def expectation_value(state, Operator):
    return round(np.dot(state.conj(), np.dot(Operator, state)).real)

