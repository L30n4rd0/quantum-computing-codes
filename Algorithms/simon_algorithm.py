'''
Created on 13 de jan de 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h
from utils.qbits import qbit_zero, qbit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi

def create_uf_gate(n_qbits):
    """
    Description:
        Make a uf gate to use on the Simon's Algorithm
        The gate is the oracle of algorithm
    Required Params:
        n_qbits: Number of qbits that algorithm will computer
        Number of qbits of the inputs X1 and X2
    Optional Params:
        None
    Return Value:
        A uf gate matrix to use on the Simon's Algorithm
    Example:
    
    """
    
    # Creating fixed Uf gate matrix to n_qbits = 2
    uf_gate_matrix = np.array(
        [
            #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#0
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#2
            [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
            [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#4
            [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#5
            [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#6
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#7
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#8
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#9
            [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#10
            [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#11
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#12
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],#13
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#14
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0] #15
        ], 
        dtype=complex
    )

    # Returning uf_gate_matrix
    return uf_gate_matrix

""" <<< MAIN >>> """
if __name__ == '__main__':
    
    # Number of qbits that algorithm will computer
    n = 2
    
    # Creating Hadamard's tensors
    tensor_h = apply_n_tensor_to(n, h)
    
    # Creating Identity's tensors
    tensor_i = apply_n_tensor_to(n, i)
    
    # Creating tensor product between:
    # Hadamard's tensors and Identity's tensors
    tensor_h_i = apply_tensor(tensor_h, tensor_i)
    
    # Creating Uf gate matrix
    uf = create_uf_gate(n)
    
    # psi_0 - Creating tensor product between inputs: X1 = |0> and X2 = |0>
    psi = apply_n_tensor_to(2 * n, qbit_zero)
    
    # psi_1 - Applying tensor_h_i to psi_0
    psi = apply_gate_to_psi(tensor_h_i, psi)
    
    # psi_2 - Applying Uf to psi_1
    psi = apply_gate_to_psi(uf, psi)
    
    # psi_3 - Applying tensor_h_i to psi_2
    psi = apply_gate_to_psi(tensor_h_i, psi)
    
    # Showing psi_3 state
#     psi = np.array(psi, dtype=float)
    print(psi)
    
