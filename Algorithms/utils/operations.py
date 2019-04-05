'''
Created on 14 de jan de 2018

@author: leonardo
'''

import numpy as np
from builtins import int
from numpy import sqrt

def apply_tensor(matrix_a, matrix_b):
    
    """
    Description:
        Make a tensor product between two matrix of any size
    Required Params:
        matrix_a: Any matrix of any size
        matrix_b: Any matrix of any size 
    Optional Params:
        None
    Return Value:
        A tensor product between two matrix of any size
    Example:
        >>> m1 = [[1,2],[3,4]]
        >>> m2 = [[1,0],[0,1]]
        >>> apply_tensor(m1, m2)
        [1, 0, 2, 0]
        [0, 1, 0, 2]
        [3, 0, 4, 0]
        [0, 3, 0, 4]
        >>> apply_tensor(m2, m1)
        [1, 2, 0, 0]
        [3, 4, 0, 0]
        [0, 0, 1, 2]
        [0, 0, 3, 4]
    """
    
    # Converting the elements of matrices to complex data type
    a, b = np.array(matrix_a, dtype = complex), np.array(matrix_b, dtype = complex)
    
    # Row and column number of matrix a
    num_row_a, num_column_a = len(a), len(a[0])
    
    # Row and column number of matrix b
    number_row_b, number_column_b = len(b), len(b[0])
    
    # Creating the tensor_result matrix and filling with ones (complex data type)
    tensor_result = np.ones((len(a) * len(b), len(a[0]) * len(b[0])), dtype=complex)
    
    # Iterating matrix a
    for row_a in range(num_row_a):
        for column_a in range(num_column_a):
            
            # Iterating matrix b
            for row_b in range(number_row_b):
                for column_b in range(number_column_b):
                    
                    # Element to insert into tensor_result matrix
                    element = a[row_a][column_a] * b[row_b][column_b]
                    
                    # Calculating the tensor row value (The number_row_b is the value to displacement, to shift, etc)
                    row_tensor = (row_a * number_row_b) + row_b
                    
                    # Calculating the tensor column value (The number_column_b is the value to displacement, to shift, etc)
                    column_tensor = (column_a * number_column_b) + column_b
                    
                    # Insert element into tensor_result matrix
                    tensor_result[row_tensor][column_tensor] = element
    
    # Returning tensor_result
    return tensor_result

def apply_n_tensor_to(tensor_number, matrix_u):
    
    """
    Description:
        Make 'n' tensor product on any gate or state in itself
    Required Params:
        tensor_number: Number of tensor product that will be applied 
        matrix_u: Any gate or state matrix of any size
    Optional Params:
        None
    Return Value:
        A 'n' tensor product on any gate in itself
    Example:
        >>> identity = [[1,0],[0,1]]
        >>> apply_n_tensor_to(2, identity)
        [[1 0 0 0]
        [0 1 0 0]
        [0 0 1 0]
        [0 0 0 1]]
    """
    
    # Converting the elements of matrix_u to complex data type
    temp_matrix = np.array(matrix_u, dtype = complex)
    
    # Initing result_matrix
    result_matrix = temp_matrix
    
    # Applying n tensor product in itself
    for i in range(tensor_number - 1):
        result_matrix = apply_tensor(result_matrix, temp_matrix)
        
    # Returning tensor result_matrix
    return result_matrix

def apply_tensor_to_matrices_vector(matrices_vector):
    
    """
    Description:
        Make tensor product between all gates or psi states on vector
    Required Params:
        matrices_vector: Any matrices vector containing gates or psi states
    Optional Params:
        None
    Return Value:
        A matrix of tensor product between all gates or psi states on vector
    Example:
        >>> identity = [[1,0],[0,1]]
        >>> apply_tensor_to_matrices_vector([identity, identity, identity])
        [[1 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0]
        [0 0 0 1 0 0 0 0]
        [0 0 0 0 1 0 0 0]
        [0 0 0 0 0 1 0 0]
        [0 0 0 0 0 0 1 0]
        [0 0 0 0 0 0 0 1]]
    """
    
    # Initing result_matrix
    result_matrix = np.array(matrices_vector[0], dtype = complex)
    
    # Applying tensor product between all matrices
    for i in range(1, len(matrices_vector)):
        result_matrix = apply_tensor(result_matrix, np.array(matrices_vector[i], dtype = complex))
        
    # Returning tensor result_matrix
    return result_matrix
    
def apply_gate_to_psi(matrix_gate, matrix_psi):
    
    """
    Description:
        Apply the gate to the psi state (Using the 'dot' operation of numpy library) 
    Required Params:
        matrix_gate: Any matrix of any gate
        matrix_psi: Matrix of any psi state 
    Optional Params:
        None
    Return Value:
        Another psi state resulting of the gate application
    Example:
        >>> psi = [[1],[0]]
        >>> x = [[0,1],[1,0]]
        >>> apply_gate_to_psi(x, psi)
        [[0],[1]]
    """
    
    # Converting the elements of matrices to complex data type
    temp_gate, temp_psi = np.array(matrix_gate, dtype = complex), np.array(matrix_psi, dtype = complex)
    
    # Applying the gate to the psi state
    psi_result = np.dot(temp_gate, temp_psi)
    
    # Returning psi_result
    return psi_result

def apply_projective_operator(operator, psi):

    # operator|psi> = (operator * |psi>) / sqrt(<psi| * operator * |psi>))
    
    # (operator * |psi>)
    result = apply_gate_to_psi(operator, psi)
    
    # operator * |psi>)    
    normalizador = np.dot(operator, psi)
    
    # transposed psi
    psi_t = np.transpose(psi)
    
    # <psi| * operator * |psi>)
    normalizador = np.dot(psi_t, normalizador)
    
    # sqrt(<psi| * operator * |psi>))
    normalizador = sqrt(normalizador)
    
    # (operator * |psi>) / sqrt(<psi| * operator * |psi>))
    result = (1 / normalizador[0][0]) * result
    
    return result

def printPSI(psi):
    
    # Qubits number 'n' used on the circuit
    n_size = np.log2(len(psi))
    n_size = int(n_size)
     
    qubit = 0
     
    for amplitude in psi:
        print( amplitude[0], '\t|%s> %d' % (np.binary_repr(qubit, n_size), qubit) )
        qubit += 1
        
#     temp = 2 * np.dot(psi, np.transpose(psi)) - np.identity(2**n_size, dtype=complex)
#     print(temp)
#     print("unitaria")
#     print(np.dot(temp, np.transpose(temp)))
    
