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

def create_n_4_qwd_gate(n_qbits, m_marked_itens):
    """
    Description:
        Make a quantum wave divider gate as specified on
        equation 22 in the article
        An N/4 fixed-point duality quantum search algorithm - 
        HAO Liang et al - 2010
    Required Params:
        n_qbits: Number of work qbits that algorithm will computer
        m_marked_itens: Number of items marked on the data base
    Optional Params:
        None
    Return Value:
        A quantum wave divider gate
    Example:

    """
    
    n_data_base_size = 2 ** n_qbits
    
    a = np.sqrt(n_data_base_size / (2 * n_data_base_size - 4 * m_marked_itens))
    b = None
    
    if m_marked_itens <= n_data_base_size / 4:
        b = np.sqrt( 
            (n_data_base_size - 4 * m_marked_itens) / 
            (2 * n_data_base_size - 4 * m_marked_itens) 
        )
        print("\nunitary v operator")
        
    else:
        b = np.sqrt( 
            (4 * m_marked_itens - n_data_base_size) / 
            (2 * n_data_base_size - 4 * m_marked_itens) 
        )
        b = np.complex(0, b)
        print("\nnon unitary v operator")
    
    
    gate_matrix = np.array(
        [[a, b],
         [b, -a]],
        dtype=complex
    )
    

    # Returning gate_matrix
    return gate_matrix


def create_controlled_u_gate(gate_matrix, controller):
    """
    Description:
        Make a quantum controlled gate to use on the CQD model
    Required Params:
        gate_matrix: numpy two-dimensional square array that 
        represents the matriz gate
        controller: value that represents the controller (0 or 1)
    Optional Params:
        None
    Return Value:
        A quantum controlled gate to use on the CQD model
    Example:

    """
    
    gate_matrix_dim = len(gate_matrix)
    
    controlled_u_gate_dim = gate_matrix_dim * 2
    
    controlled_u_gate = np.identity(n=controlled_u_gate_dim, dtype=complex)
    
    shift = 2
    shift_extra = controller
    
    for row in range(gate_matrix_dim):
        for column in range(gate_matrix_dim):
            controlled_u_gate[row * shift + shift_extra] \
            [column * shift + shift_extra] = gate_matrix[row][column]
            
    return controlled_u_gate
    
    
    