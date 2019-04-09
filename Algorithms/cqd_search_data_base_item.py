'''
Created on Feb 2, 2019

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
        [[0. + 0.j, 0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, 0.5 + 0.j],
         [0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j],
         [0. + 0.j, 0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, -0.5 + 0.j],
         [0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j],
         [0. + 0.j, 0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, -0.5 + 0.j],
         [0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j],
         [0. + 0.j, 0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, 0.5 + 0.j],
         [0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, -0.5 + 0.j, 0. + 0.j, 0.5 + 0.j, 0. + 0.j]],
        dtype=complex
    )

    # Returning o_gate_matrix
    return o_gate_matrix


if __name__ == '__main__':

    # Number of qbits that algorithm will computer
    n = 5

    # Item to search: |111....11>
    item_to_search = apply_n_tensor_to(n + 1, qubit_one)

    item_to_search_projector = np.dot(item_to_search, np.transpose(item_to_search))
    print("\nitem_to_search_projector")
    print(item_to_search_projector)

    # Creating Identity's tensors to works qubits
    tensor_i = np.identity(2 ** n, dtype=complex)

    # Creating oracle
    oracle = apply_tensor(tensor_i, i)
    print("\noraculo")
    print(oracle)

    oracle = oracle - (2 * item_to_search_projector)
    print("\noraculo")
    print(oracle)

    # Creating controled_u
    controlled_u_1 = apply_tensor(tensor_i, z)
    #     controlled_u_1 = (2 * item_to_search_projector) + controlled_u_1

    print("\ncontrolled_u_1")
    print(controlled_u_1)

    # Creating Hadamard's tensors, works and auxiliary qubis
    tensor_h = apply_n_tensor_to(n + 1, h)

    # Creating tensor Identity_Hadamard
    tensor_i_h = apply_tensor(tensor_i, h)

    # Creating projective_operator
    projective_operator = apply_tensor(tensor_i, np.dot(qubit_zero, np.transpose(qubit_zero)))

    # psi_0 - Creating tensor product between inputs: |000000>
    psi = apply_n_tensor_to(n + 1, qubit_zero)
    print('\npsi_0 - Creating tensor product between inputs: |000000>\n')
    printPSI(psi)

    #     print(create_qwd(3))

    # psi_1 - Applying tensor_h (divider) to psi_0
    psi = apply_gate_to_psi(tensor_h, psi)
    print('\npsi_1 - Applying tensor_h (divider) to psi\n')
    printPSI(psi)

    # psi_2 - Applying oracle to psi_1
    psi = apply_gate_to_psi(oracle, psi)
    print('\npsi_2 - Applying oracle to psi\n')
    printPSI(psi)

    # psi_3 - Applying controlled_u_1 to psi_2
    psi = apply_gate_to_psi(controlled_u_1, psi)
    print('\npsi_3 - Applying controlled_u_1 to psi\n')
    printPSI(psi)

    # psi_4 - Applying tensor_i_h (combiner) to psi_3
    psi = apply_gate_to_psi(tensor_i_h, psi)
    print('\npsi_4 - Applying (combiner) to psi\n')
    printPSI(psi)

    print("Projective")
    print(projective_operator)

    # psi_5 - Applying projective_operator to psi_4
    psi = apply_projective_operator(projective_operator, psi)
    print('\npsi_5 - Applying projective_operator to psi\n')
    printPSI(psi)
