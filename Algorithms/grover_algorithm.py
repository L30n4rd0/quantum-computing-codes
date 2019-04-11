'''
Created on 13 de jan de 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h
from utils.qbits import qubit_zero, qubit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi

def create_phase_inversion_gate(n_qbits, index_qbit):
    """
    Description:
        Make the phase inversion gate that mark (inverts the signal) the index qubit received as a parameter
        The gate is the oracle of algorithm
    Required Params:
        n_qbits - Number of qbits that algorithm will computer
        index_qbit - Index number of qbit that gate will mark
    Optional Params:
        None
    Return Value:
        A phase inversion gate
    Example:
        >>> phase_inversion = create_phase_inversion_gate(2, 2)
        >>> psi = 
        [[ 0.5+0.j]
         [ 0.5+0.j]
         [ 0.5+0.j]
         [ 0.5+0.j]]
        >>> apply_gate_to_psi(phase_inversion, psi)
        [[ 0.5+0.j]
         [ 0.5+0.j]
         [-0.5+0.j]
         [ 0.5+0.j]]
    """
    
    # Creating matrix phase_inversion_gate
    phase_inversion_gate = np.identity(2**n_qbits, dtype=complex)
    
    # Marking the index qbit
    phase_inversion_gate[index_qbit][index_qbit] *= -1
    
    # Returning phase_inversion_gate
    return phase_inversion_gate

def create_inversion_about_mean_gate(n_qbits):
    """
    Description:
        Make the inversion about mean to psi state
    Required Params:
        n_qbits - Number of qbits that algorithm will computer
    Optional Params:
        None
    Return Value:
        A inversion about mean gate
    Example:
        >>> inversion_about_mean = create_inversion_about_mean_gate(2)
        >>> psi = 
        [[ 0.5+0.j]
         [ 0.5+0.j]
         [-0.5+0.j]
         [ 0.5+0.j]]
        >>> apply_gate_to_psi(inversion_about_mean, psi)
        [[ 0.+0.j]
         [ 0.+0.j]
         [ 1.+0.j]
         [ 0.+0.j]]
        
    """
    
    # Creating matrix inversion_about_mean (filling of ones)
    inversion_about_mean_gate = np.ones((2**n_qbits, 2**n_qbits), dtype=complex)
    
    # Dividing elements by 2**n
    inversion_about_mean_gate /= 2**n
    
    # <<<Doing the operation: −I + 2 * (inversion_about_mean_gate)>>>
    
    # Doing: 2 * (inversion_about_mean_gate)
    inversion_about_mean_gate *= 2
    
    # Creating identity matrix
    i_matrix = np.identity(2**n, dtype=complex)
    
    # Doing: -1 * i_matrix
    i_matrix *= -1
    
    # Doing: −I + 2 * (inversion_about_mean_gate)
    inversion_about_mean_gate = inversion_about_mean_gate + i_matrix
    
    # Returning inversion_about_mean_gate
    return inversion_about_mean_gate


""" <<< MAIN >>> """
if __name__ == '__main__':
    
    # Number of qbits that algorithm will computer
    n = 8
    
    # Index number of qbit that oracle gate will mark
    # For example: the penultimate qbit index number (2**n - 2)
    index = 2**n - 2
    
    # Creating Hadamard's tensors
    tensor_h = apply_n_tensor_to(n, h)
    
    # Creating phase inversion gate (Oracle, Uf)
    phase_inversion = create_phase_inversion_gate(n, index)
    
    # Creating inversion about mean gate
    inversion_about_mean = create_inversion_about_mean_gate(n)
    
    # psi_0 - applying tensor to zeros qbits
    psi = apply_n_tensor_to(n, qubit_zero)
    print('\npsi_0 - applying tensor to zeros qbits')
    print(psi)
    
    # psi_1 - applying Hadamard's tensors to psi_0
    psi = apply_gate_to_psi(tensor_h, psi)
    print('\npsi_1 - applying Hadamards tensors to psi_0')
    print(psi)
    
    # Applying phase inversion gate and inversion about mean gate ( sqrt(2**n) times )
    for i in range( int(np.sqrt(2**n)) ):
        
        # psi_2 - applying phase inversion gate to psi_1
        psi = apply_gate_to_psi(phase_inversion, psi)
        print('\npsi_2.%d applying phase inversion gate' % (i + 1))
        print(psi)
        
        # psi_3 - applying inversion about mean gate to psi_2
        psi = apply_gate_to_psi(inversion_about_mean, psi)
        print('\npsi_3.%d applying inversion about mean gate' % (i + 1))
        print(psi)
    
