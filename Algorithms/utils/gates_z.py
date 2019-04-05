'''
Created on 14 de fev de 2019

@author: leonardo
'''

import numpy as np

cz_q_1_q_0 = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0,-1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0,-1]]
)

cz_q_2_q_1 = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0,-1, 0],
     [0, 0, 0, 0, 0, 0, 0,-1]]
)

cz_q_2_q_0 = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0,-1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0,-1]]
)

z_q_2 = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0,-1, 0, 0, 0],
     [0, 0, 0, 0, 0,-1, 0, 0],
     [0, 0, 0, 0, 0, 0,-1, 0],
     [0, 0, 0, 0, 0, 0, 0,-1]]
)

z_q_1 = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0,-1, 0, 0, 0, 0, 0],
     [0, 0, 0,-1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0,-1, 0],
     [0, 0, 0, 0, 0, 0, 0,-1]]
)

z_q_0 = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0,-1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0,-1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0,-1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0,-1]]
)
 
fredkin = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1]]
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
    c_n_not_gate = np.identity(matrix_size)
    
    c_n_not_gate[matrix_size - 1][matrix_size - 1] = 0
    c_n_not_gate[matrix_size - 2][matrix_size - 2] = 0
    c_n_not_gate[matrix_size - 1][matrix_size - 2] = 1
    c_n_not_gate[matrix_size - 2][matrix_size - 1] = 1
    
    return c_n_not_gate
