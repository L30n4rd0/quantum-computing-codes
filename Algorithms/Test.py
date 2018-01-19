'''
Created on 16 de jan de 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h, c_not
from utils.qbits import qbit_zero, qbit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, apply_tensor_to_matrices_vector

if __name__ == '__main__':
    
    # Tensor 2 Hadamard
    tensor_h = apply_tensor_to_matrices_vector([h, h, h])
    
    # psi_0 - tensor to qbits|111>
    psi = apply_tensor_to_matrices_vector([qbit_zero, qbit_zero, qbit_one])
    
    # psi_1 - applying tensor_h to psi_0
    psi = apply_gate_to_psi(tensor_h, psi)
    
    # Show psi_1 state
    print(psi)
    
    