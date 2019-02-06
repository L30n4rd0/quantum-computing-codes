'''
Created on May 22, 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h, f
from utils.qbits import qubit_zero, qubit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, printPSI
from numpy import float, sqrt

"""
Constant used to create the non unitary matrix
"""
a  = 0.6

def create_n_a_gate():
    
    n_a = np.array(
        [
            [1,0],
            [0,a],
        ], 
        dtype=complex
    )
    
    return n_a

def create_u_a_gate():
    
    n_a = np.array(
        [
            [a, sqrt(1 - (a**2))],
            [sqrt(1 - (a**2)), -1 * a],
        ], 
        dtype=complex
    )
    
    return n_a

def create_n_a_gate_v2():
    
    matrix_size = 4
    
    c_n_u_gate = np.identity(matrix_size, dtype=complex)
    
    c_n_u_gate[matrix_size - 1][matrix_size - 1] = -1 * a
    c_n_u_gate[matrix_size - 2][matrix_size - 2] = a
    c_n_u_gate[matrix_size - 1][matrix_size - 2] = sqrt(1 - (a**2))
    c_n_u_gate[matrix_size - 2][matrix_size - 1] = sqrt(1 - (a**2))
    
    n_zero = np.zeros((2, 2), dtype=complex)
    n_zero[0][0] = 1
    
    i_n_zero_tensor = apply_tensor(np.identity(2, dtype=complex), n_zero)
    
    n_a_gate_v2 = apply_gate_to_psi(c_n_u_gate, i_n_zero_tensor)
    
    return n_a_gate_v2

def create_controlled_n_a_gate_v1(n_qbits):
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
    
    matrix_size = 2**n_qbits
    
    # Creating matrix identity
    c_n_a_gate = np.identity(matrix_size, dtype=complex)
    
    c_n_a_gate[matrix_size - 1][matrix_size - 1] = a

    # Returning n_a
    return c_n_a_gate

def create_controlled_n_a_gate_with_ancilla(n_qbits):
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
    
    matrix_size = 2**n_qbits
    
    # Creating matrix identity
    c_n_not_gate = np.identity(matrix_size, dtype=complex)
    
    c_n_not_gate[matrix_size - 1][matrix_size - 1] = 0
    c_n_not_gate[matrix_size - 2][matrix_size - 2] = 0
    c_n_not_gate[matrix_size - 1][matrix_size - 2] = 1
    c_n_not_gate[matrix_size - 2][matrix_size - 1] = 1
    
    identity_tensor = np.identity(int(matrix_size / 2), dtype=complex)
    
    n_a_gate = create_n_a_gate()
    
    identity_n_a_tensor = apply_tensor(identity_tensor, n_a_gate)
    
    controlled_n_a_gate_with_ancilla = apply_gate_to_psi(identity_n_a_tensor , c_n_not_gate)
    
    controlled_n_a_gate_with_ancilla = apply_gate_to_psi(c_n_not_gate, controlled_n_a_gate_with_ancilla)
    
    # Returning controlled_n_a_gate_with_ancilla
    return controlled_n_a_gate_with_ancilla

def create_d_gate(n_qbits):
    
    c_n_a_gate = create_controlled_n_a_gate_v1(n_qbits)
#     print('\nc_n_a_gate')
#     print(np.array(c_n_a_gate, dtype = float))
    
    x_tensor = apply_n_tensor_to(n_qbits, x)
#     print('\nx_tensor')
#     print(np.array(x_tensor, dtype = float))
    
    i_x_tensor = apply_tensor(apply_n_tensor_to(n_qbits - 1, i), x)
#     print('\ni_x_tensor')
#     print(np.array(i_x_tensor, dtype = float))
    
    d_gate = x_tensor
    
    d_gate = apply_gate_to_psi(c_n_a_gate, d_gate)
     
    d_gate = apply_gate_to_psi(i_x_tensor, d_gate)
      
    d_gate = apply_gate_to_psi(c_n_a_gate, d_gate)
      
    d_gate = apply_gate_to_psi(x_tensor, d_gate)
      
    d_gate = apply_gate_to_psi(c_n_a_gate, d_gate)
      
    d_gate = apply_gate_to_psi(i_x_tensor, d_gate)
      
    d_gate = apply_gate_to_psi(c_n_a_gate, d_gate)
    
    return d_gate

def testing_d_gate(n_qbits):
    n = n_qbits
    
    d_gate = create_d_gate(n)
    print('\nd_gate\n', d_gate)
#     print(np.array(d_gate, dtype = float))
    
    psi = apply_n_tensor_to(n, qubit_one)
    print('\ninitial psi')
    printPSI(psi)
    
    psi = apply_gate_to_psi(d_gate, psi)
    print('\napplying d_gate to psi')
    printPSI(psi)
    
def testing_controlled_n_a_gate_v1(n_qbits):
    n = n_qbits
 
    controlled_n_a_gate = create_controlled_n_a_gate_v1(n)
    print('\nc_n_a_gate version 1\n', controlled_n_a_gate)
#     print(np.array(controlled_n_a_gate, dtype = float))
 
    psi = apply_tensor(qubit_one, qubit_one)
    psi = apply_tensor(psi, qubit_one)
    print('\npsi inicial')
    printPSI(psi)
     
    psi = apply_gate_to_psi(controlled_n_a_gate, psi)
    print('\napplying controlled_n_a_gate to psi')
    printPSI(psi)
     
def testing_controlled_n_a_gate_with_ancilla(n_qbits):
    n = n_qbits
 
    controlled_n_a_gate_with_ancilla = create_controlled_n_a_gate_with_ancilla(n + 1)
    print('\ncontrolled_n_a_gate_with_ancilla\n', controlled_n_a_gate_with_ancilla)
#     print(np.array(controlled_n_a_gate, dtype = float))
 
    psi = apply_tensor(qubit_one, qubit_one)
    psi = apply_tensor(psi, qubit_one)
    print('\npsi inicial')
    printPSI(psi)
     
    psi = apply_gate_to_psi(controlled_n_a_gate_with_ancilla, apply_tensor(psi, qubit_zero))
    print('\napplying controlled_n_a_gate_with_ancilla to psi')
    printPSI(psi)
    
def comparing_n_a_gate_v1_and_n_a_gate_with_ancilla(n_qbits):
    n = n_qbits
    
    controlled_n_a_gate = create_controlled_n_a_gate_v1(n)
    print('\nc_n_a_gate version 1\n', controlled_n_a_gate)
#     print(np.array(controlled_n_a_gate, dtype = float))
 
    controlled_n_a_gate_with_ancilla = create_controlled_n_a_gate_with_ancilla(n + 1)
    print('\nc_n_a_gate with ancilla\n', controlled_n_a_gate_with_ancilla)
#     print(np.array(controlled_n_a_gate_with_ancilla, dtype = float))
     
    psi = apply_tensor(qubit_one, qubit_one)
    psi = apply_tensor(psi, qubit_one)
    print('\npsi inicial')
    printPSI(psi)
     
    psi_temp = apply_gate_to_psi(controlled_n_a_gate, psi)
    print('\napply controlled_n_a_gate to psi')
    printPSI(psi_temp)
     
    psi_temp = apply_gate_to_psi(controlled_n_a_gate_with_ancilla, apply_tensor(psi, qubit_zero))
    print('\napply controlled_n_a_gate_with_ancilla to psi')
    printPSI(psi_temp)
    

if __name__ == '__main__':
    
    n = 3
    
#     testing_d_gate(n)
#     testing_controlled_n_a_gate_v1(n)
#     testing_controlled_n_a_gate_with_ancilla(n)
#     comparing_n_a_gate_v1_and_n_a_gate_with_ancilla(n)
    print(create_n_a_gate_v2())
    
