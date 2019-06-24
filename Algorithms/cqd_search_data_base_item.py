"""
Created on Feb 2, 2019

@author: leonardo
"""


import numpy as np
from utils.gates import i, z, h
from utils.operations import apply_tensor, apply_n_tensor_to, \
apply_gate_to_psi, print_psi, apply_projective_operator, plot_psi
from utils.qbits import qubit_one, qubit_zero

############################################################
####### Circuit Properties #################################
############################################################
# Number of qbits that algorithm will computer
n = 4

# Item to search: |111....11>
item_to_search = apply_n_tensor_to(n + 1, qubit_one)

############################################################
####### Circuit Gates ######################################
############################################################
item_to_search_projector = np.dot(item_to_search, np.transpose(item_to_search))
print("\nitem_to_search_projector")
print(item_to_search_projector)

# Creating Identity"s tensors to works qubits
tensor_i = np.identity(2 ** n, dtype=complex)

# Creating oracle
oracle = apply_tensor(tensor_i, i)
print("\noraculo")
print(oracle)

oracle = oracle - (2 * item_to_search_projector)
print("\noraculo")
print(oracle)

# Creating controled_u_1
controlled_u_1 = apply_tensor(tensor_i, z)
#     controlled_u_1 = (2 * item_to_search_projector) + controlled_u_1

print("\ncontrolled_u_1")
print(controlled_u_1)

# Creating Hadamard"s tensors, works and auxiliary qubis
tensor_h = apply_n_tensor_to(n + 1, h)

# Creating tensor Identity_Hadamard
tensor_i_h = apply_tensor(tensor_i, h)

# Creating projection_operator
projection_operator = apply_tensor(
    tensor_i, 
    np.dot(qubit_zero, np.transpose(qubit_zero))
)

############################################################
####### Circuit Execution ##################################
############################################################
# psi_0 - Creating tensor product between inputs: |000000>
psi = apply_n_tensor_to(n + 1, qubit_zero)
print("\npsi_0 - Creating tensor product between inputs: |000000>\n")
print_psi(psi)

# psi_1 - Applying tensor_h (divider) to psi_0
psi = apply_gate_to_psi(tensor_h, psi)
print("\npsi_1 - Applying tensor_h (divider) to psi\n")
print_psi(psi)

# psi_2 - Applying oracle to psi_1
psi = apply_gate_to_psi(oracle, psi)
print("\npsi_2 - Applying oracle to psi\n")
print_psi(psi)

# psi_3 - Applying controlled_u_1 to psi_2
psi = apply_gate_to_psi(controlled_u_1, psi)
print("\npsi_3 - Applying controlled_u_1 to psi\n")
print_psi(psi)

# psi_4 - Applying tensor_i_h (combiner) to psi_3
psi = apply_gate_to_psi(tensor_i_h, psi)
print("\npsi_4 - Applying (combiner) to psi\n")
print_psi(psi)
plot_psi(
    psi, 
    'plots_cqd_search_data_base_item/' + 
    'cqd_search_data_base_item_plots_before_projection_operator_' + 
    '1_marked_itens.png'
)

# psi_5 - Applying projection_operator to psi_4
psi = apply_projective_operator(projection_operator, psi)
print("\npsi_5 - Applying projection_operator to psi\n")
print_psi(psi)
plot_psi(
    psi, 
    'plots_cqd_search_data_base_item/' + 
    'cqd_search_data_base_item_plots_after_projection_operator_' + 
    '1_marked_itens.png'
)
    