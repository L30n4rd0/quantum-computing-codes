'''
Created on 16 de jan de 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h, c_not
from utils.qbits import qbit_zero, qbit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, apply_tensor_to_matrices_vector, printPSI

# Creating gate matrix - Uf Luciano's example
#     uf_gate_matrix = np.array(
#         [
#             #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#             [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#0
#             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1
#             [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#2
#             [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
#             [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#4
#             [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#5
#             [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#6
#             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#7
#             [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#8
#             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#9
#             [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#10
#             [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#11
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],#12
#             [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#13
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],#14
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0] #15
#         ], 
#         dtype=complex
#     )

if __name__ == '__main__':
    
    # Tensor 2 Hadamard
    tensor_h = apply_tensor_to_matrices_vector([h, h, h])
    
    # psi_0 - tensor to qbits|111>
    psi = apply_tensor_to_matrices_vector([qbit_zero, qbit_zero, qbit_one])
    
    # psi_1 - applying tensor_h to psi_0
    psi = apply_gate_to_psi(tensor_h, psi)
    
    # Show psi_1 state
    printPSI(psi)
    
    