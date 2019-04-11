'''
Created on 14 de jan de 2018

@author: leonardo
'''

import numpy as np

'''Pauli-identity gate'''
i = np.identity(2, dtype=complex)

'''Pauli-X gate (NOT gate)'''
x = np.array(
    [[0, 1],
     [1, 0]],
    dtype=complex
)

'''Pauli-Y gate'''
y = np.array(
    [[0, 0. - 1.j],
     [0. + 1.j, 0]],
    dtype=complex
)

'''Pauli-Z gate (fase gate)'''
z = np.array(
    [[1, 0],
     [0, -1]],
    dtype=complex
)

'''Hadamard (H) gate'''
h = np.array(
    [[1/np.sqrt(2), 1/np.sqrt(2)],
     [1/np.sqrt(2), -1/np.sqrt(2)]],
    dtype=complex
)

'''Controlled NOT gate'''
c_not = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]],
    dtype=complex
)

'''Fredkin (F) gate'''
f = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1]],
    dtype=complex
)

def create_controlled_n_not(n_controls):
    """
    Description:
        Make a controlled_not gate with n controls
    Required Params:
        n_controls: Number of qbits of controls used on the gate
    Optional Params:
        None
    Return Value:
        A controlled_not gate with n controls
    Example:
    
    """
    
    matrix_size = 2** (n_controls + 1)
    
    # Creating matrix identity
    c_n_not_gate = np.identity(matrix_size, dtype=complex)
    
    c_n_not_gate[matrix_size - 1][matrix_size - 1] = 0
    c_n_not_gate[matrix_size - 2][matrix_size - 2] = 0
    c_n_not_gate[matrix_size - 1][matrix_size - 2] = 1
    c_n_not_gate[matrix_size - 2][matrix_size - 1] = 1
    
    return c_n_not_gate

