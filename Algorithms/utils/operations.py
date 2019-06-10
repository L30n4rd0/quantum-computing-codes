'''
Created on 14 de jan de 2018

@author: leonardo
'''

import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt



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
        [[1, 0, 2, 0]
        [0, 1, 0, 2]
        [3, 0, 4, 0]
        [0, 3, 0, 4]]
        >>> apply_tensor(m2, m1)
        [[1, 2, 0, 0]
        [3, 4, 0, 0]
        [0, 0, 1, 2]
        [0, 0, 3, 4]]
    """
    
    # Converting the elements of matrices to complex data type
    a, b = np.array(matrix_a, dtype = complex), np.array(matrix_b, dtype = complex)
    
    # Row and column number of matrix a
    num_row_a, num_column_a = len(a), len(a[0])
    
    # Row and column number of matrix b
    num_row_b, num_column_b = len(b), len(b[0])
    
#     tensor = np.tensordot(a, b, axes=0)
#     
#     temp = np.array([], dtype=complex)
#     
#     for row_0 in tensor:
#         for index in range(num_row_b):
#             for row_1 in row_0:
#                 temp = np.append(temp, row_1[index])
# 
#     tensor_result = np.reshape(temp, (num_row_a * num_row_b, num_column_a * num_column_b))
    
    
    
    
    # Creating the tensor_result matrix and filling with ones (complex data type)
    tensor_result = np.ones((num_row_a * num_row_b, num_column_a * num_column_b), dtype=complex)
    # Iterating matrix a
    for row_a in range(num_row_a):
        for column_a in range(num_column_a):
             
            # Iterating matrix b
            for row_b in range(num_row_b):
                for column_b in range(num_column_b):
                     
                    # Element to insert into tensor_result matrix
                    element = a[row_a][column_a] * b[row_b][column_b]
                     
                    # Calculating the tensor row value (The num_row_b is the value to displacement, to shift, etc)
                    row_tensor = (row_a * num_row_b) + row_b
                     
                    # Calculating the tensor column value (The num_column_b is the value to displacement, to shift, etc)
                    column_tensor = (column_a * num_column_b) + column_b
                     
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



def calculate_probabilities(psi):
    probabilities = []
    
    for amplitude in psi:
        probability = amplitude[0] * np.conjugate(amplitude[0])
        probabilities.append(probability.real)
    
    return probabilities
    


def calculate_binary_values_states(psi):
    
    # Qubits number 'n' used on the circuit
    n_size = np.log2(len(psi))
    n_size = int(n_size)
     
    states = []
    
    for index in range(len(psi)):
        states.append( str(np.binary_repr(index, n_size)) )
        
    return states




def print_psi(psi):
    
    states = calculate_binary_values_states(psi)
    
    for index in range(len(psi)):
        print( psi[index][0], '\t|%s> %d' % (states[index], index) )
    
    
    print("Norma:")
    print_psi_norm(psi)
        


def print_psi_norm(psi):
    norm = sum(calculate_probabilities(psi))
    print(norm)
    
    
    
def plot_psi(psi, address_to_save):
    
    # Qubits number 'n' used on the circuit
    n_size = np.log2(len(psi))
    n_size = int(n_size)
     
    states = calculate_binary_values_states(psi)
    probabilities = calculate_probabilities(psi)
    
    plt.title("Gráfico de probabilidades")
    plt.xlabel("Estados")
    plt.ylabel("Probabilidades")
    
    plt.bar(x=states, height=probabilities, width=0.8, bottom=None)
    plt.xticks(rotation=70)
    # plt.legend(["Probabilidades"])
    
    # Automatically adjust subplot parameters
    plt.tight_layout()
    
    # Showing the graph
#     plt.show()

    # Saving the figure with better resolution
    plt.savefig(address_to_save, dpi=300)
    
    # Clear the entire current figure with all its axes
    plt.clf()
    
    # Close the current figure window
    plt.close()

