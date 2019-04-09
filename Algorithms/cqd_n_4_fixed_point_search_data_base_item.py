'''
Created on April 5, 2019

Simulation of the article An N:4 fixed-point duality quantum search algorithm - HAO Liang et al - 2010

@author: leonardo
'''


import numpy as np
from utils.gates import i, x, y, z, h, f, c_not
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, printPSI, apply_projective_operator
from utils.gates_z import cz_q_1_q_0, cz_q_2_q_0
from utils.qbits import qubit_one, qubit_zero

def create_qwd(n_qbits):
    """
    Description:
        Make a quantum wave divider gate as specified on
        step 2 in the article
    Required Params:
        n_qbits: Number of qbits that algorithm will computer
    Optional Params:
        None
    Return Value:
        A quantum wave divider gate
    Example:

    """
    
    base_size = 2**n_qbits
    a = np.sqrt( base_size / (2 * base_size - 4) )
    b = np.sqrt( (base_size - 4) / (2 * base_size - 4) )

    gate_matrix = np.array(
        [[a, b],
         [b, -a]],
        dtype=complex
    )

    # Returning gate_matrix
    return gate_matrix



if __name__ == '__main__':

    # Number of qbits that algorithm will computer
    n = 5
    

    # Item to find: |111....11>
    item_to_search = apply_n_tensor_to(n, qubit_one)
    

    # Creating projector operator to item to search
    item_to_search_projector = np.dot(item_to_search, np.transpose(item_to_search))
    print("\nitem_to_search_projector")
    print(item_to_search_projector)


    # Creating Identity's tensors to work qubits
    tensor_i = np.identity(2 ** n, dtype=complex)



    # Creating oracle
    # On the article, in step 1, the oracle is defined as:
    # u_t = I - 2 * item_to_search_projector
    oracle = tensor_i - (2 * item_to_search_projector)
    print("\noraculo")
    print(oracle)
    
    
    
    # Creating qwd. On the article it is defined as
    # v in step 2
    v = create_qwd(n)
    print("\nv")
    print(v)
    
#     v_t = np.conjugate(v)
#     v_t = np.transpose(v_t)
#     
#     printPSI("\n")
#     print(np.dot(v, v_t))
    
    
     
    # Creating Hadamard's tensors, works
    tensor_h = apply_n_tensor_to(n, h)
    print("tensor_h")
    print(tensor_h)
 
 
 
    # Creating controled_u_0
    # On the article is:
    # u_s = 2 * item_to_search_projector - I
    # controlled_u_0 = 2 * item_to_search_projector - tensor_i
 
    controlled_u_0 = apply_tensor(tensor_i, i)
     
    matrix_size = len(controlled_u_0)
     
#     for index in range(0, matrix_size, 2):
#         controlled_u_0[index][index] = -1
     
    controlled_u_0[matrix_size - 2][matrix_size - 2] = -1
 
    print("\ncontrolled_u_0")
    print(controlled_u_0)
     
 
 
 
    # Creating controled_u_1 - invert all sings
    controlled_u_1 = apply_tensor(tensor_i, z)
    print("\ncontrolled_u_1")
    print(controlled_u_1)
      
      
  
    # Creating projective_operator
    projective_operator = apply_tensor(tensor_i, np.dot(qubit_zero, np.transpose(qubit_zero)))
    print("\nprojective_operator")
    print(projective_operator)
      
      
   
    # psi_0 - Creating tensor product between inputs: |000000>
    psi = apply_n_tensor_to(n + 1, qubit_zero)
    print('\npsi_0 - Creating tensor product between inputs: |000000>\n')
    printPSI(psi)
         
     
    # psi_1 - Applying tensor_h to psi_0 on work qubits
    psi = apply_gate_to_psi( apply_tensor(tensor_h, i), psi )
    print('\npsi_1 - Applying tensor_h to psi_0 on work qubits\n')
    printPSI(psi)
        
     
    # psi_2 - Applying oracle to psi_1
    psi = apply_gate_to_psi( apply_tensor(oracle, i), psi )
    print('\npsi_2 - Applying oracle to psi\n')
    printPSI(psi)
        
        
    # psi_3 - Applying v (qwd) to psi_2
    psi = apply_gate_to_psi( apply_tensor(tensor_i, v), psi )
    print('\npsi_3 - Applying v (qwd) to psi_2\n')
    printPSI(psi)
    
    
    
    
    # psi_4 - Applying controlled_u_0 to psi_3
    psi = apply_gate_to_psi(controlled_u_0, psi)
    print('\npsi_4 - Applying controlled_u_0 to psi_3\n')
    printPSI(psi)
      
   
     
    # psi_5 - Applying controlled_u_1 to psi_4
    psi = apply_gate_to_psi(controlled_u_1, psi)
    print('\npsi_5 - Applying controlled_u_1 to psi\n')
    printPSI(psi)
     
  
  
    # psi_6 - Applying conjugated transposed of v (qwc) to psi
    v = np.conjugate(v)
    v = np.transpose(v)
    psi = apply_gate_to_psi( apply_tensor(tensor_i, v), psi )
    print('\npsi_6 - Applying conjugated transposed of v (qwc) to psi\n')
    printPSI(psi)
  
  
#     print("Projective")
#     print(projective_operator)
# 
  
#     # psi_5 - Applying projective_operator to psi_4
#     psi = apply_projective_operator(projective_operator, psi)
#     print('\npsi_5 - Applying projective_operator to psi\n')
#     printPSI(psi)
