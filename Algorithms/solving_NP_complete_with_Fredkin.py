'''
Created on 24 de abr de 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h, f
from utils.qbits import qubit_zero, qubit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, printPSI

def create_o_gate(n_qbits):
    """
    Description:
        Make a non unitary O gate
    Required Params:
        n_qbits: Number of qbits that algorithm will computer
    Optional Params:
        None
    Return Value:
        A non unitary O gate
    Example:
    
    """
    
    o_gate_matrix = np.array(
        [
            [0,0],
            [0,np.power(2, n_qbits)],
        ], 
        dtype=complex
    )

    # Returning o_gate_matrix
    return o_gate_matrix

if __name__ == '__main__':
    # Number of qbits that algorithm will computer
    n = 6
    
    # Creating Hadamard's tensors
    tensor_h = apply_n_tensor_to(n, h)
    
    # Creating Fredkin's tensors
    tensor_f = apply_n_tensor_to(int(n/3), f)
    
    # Creating Indentity's tensors
    tensor_i = apply_n_tensor_to(n - 1, i)
    
    # Creating O operator
    tensor_o_i = apply_tensor(create_o_gate(n), tensor_i)
    
    # psi_0 - Creating tensor product between inputs: |000000>
    psi = apply_n_tensor_to(n, qubit_zero)
    print('\npsi_0 - Creating tensor product between inputs: |000000>')
    printPSI(psi);
    
    # psi_1 - Applying tensor_h to psi_0
    psi = apply_gate_to_psi(tensor_h, psi)
    print('\npsi_1 - Applying tensor_h to psi_0')
    printPSI(psi);
    
    # psi_2 - Applying tensor_f to psi_1
    psi = apply_gate_to_psi(tensor_f, psi)
    print('\npsi_2 - Applying tensor_f to psi_2')
    printPSI(psi);
    
    # psi_3 - Applying tensor_o_i to psi_2
    psi = apply_gate_to_psi(tensor_o_i, psi)
    print('\npsi_3 - Applying tensor_o_i to psi_3')
    printPSI(psi);
    
